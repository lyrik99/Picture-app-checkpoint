import tkinter as tk
from PIL import Image, ImageTk
import cv2
import numpy as np

class ImageAnalyzer:
    def __init__(self, image):
        self.image = image

    def analyze_image(self):
        # Преобразуем изображение в формат OpenCV
        open_cv_image = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2BGR)
        gray_image = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
        blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
        edges = cv2.Canny(blurred_image, 50, 150)

        # Поиск контуров
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        results = []

        for i, contour in enumerate(contours):
            if cv2.contourArea(contour) < 100: # Игнорируем мелкие объекты
                continue

            # Аппроксимация контура
            epsilon = 0.02 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            # Определяем форму объекта
            if len(approx) == 4:
                shape = "Прямоугольник"
            else:
                # Приближаем контур до эллипса
                if len(approx) > 5:
                    ellipse = cv2.fitEllipse(approx)
                    (center, axes, angle) = ellipse
                    major_axis, minor_axis = max(axes), min(axes)
                    aspect_ratio = major_axis / minor_axis
                    if aspect_ratio < 1.2: # Учитываем круги и почти круги
                        shape = "Круг"
                    else:
                        shape = "Овал"
                else:
                    shape = "Неопределено"

            # Рисуем контуры и аннотации на изображении
            cv2.drawContours(open_cv_image, [approx], 0, (0, 255, 0), 2) # Рисуем контур
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
            else:
                cX, cY = 0, 0
            text = f"ID{i + 1}"
            cv2.putText(open_cv_image, text, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            x, y, w, h = cv2.boundingRect(contour)
            results.append((i + 1, shape, w, h))

        # Отображаем аннотированное изображение
        annotated_image = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2RGB)
        annotated_image_pil = Image.fromarray(annotated_image)
        annotated_image_tk = ImageTk.PhotoImage(annotated_image_pil)

        # Создаем окно с таблицей и аннотированным изображением
        result_window = tk.Toplevel()
        result_window.title("Analysis Results")

        # Отображаем таблицу результатов
        result_text = tk.Text(result_window, height=15, width=50)
        result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        result_text.insert(tk.END, "ID\tФорма\tШирина\tВысота\n")
        result_text.insert(tk.END, "-" * 40 + "\n")

        for obj in results:
            result_text.insert(tk.END, f"{obj[0]}\t{obj[1]}\t{obj[2]:.2f}\t{obj[3]:.2f}\n")
        result_text.config(state=tk.DISABLED)

        # Отображаем аннотированное изображение
        image_label = tk.Label(result_window, image=annotated_image_tk)
        image_label.image = annotated_image_tk
        image_label.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
