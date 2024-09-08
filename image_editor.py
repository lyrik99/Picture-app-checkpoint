import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageEnhance, ImageTk
from image_analyzer import ImageAnalyzer

class ImageEditor:
    def __init__(self, image, root):
        self.image = image
        self.root = root

    def open_editor_window(self):
        # Открываем новое всплывающее окно
        self.editor_window = tk.Toplevel()
        self.editor_window.title("Image Editor")

        # Создаем Canvas с прокруткой
        self.canvas = tk.Canvas(self.editor_window)
        self.scroll_x = tk.Scrollbar(self.editor_window, orient="horizontal", command=self.canvas.xview)
        self.scroll_y = tk.Scrollbar(self.editor_window, orient="vertical", command=self.canvas.yview)

        self.canvas.config(xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        # Размещаем Canvas и полосы прокрутки в окне
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        # Создаем фрейм внутри Canvas для размещения изображения
        self.image_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.image_frame, anchor="nw")

        # Кнопка для изменения контрастности
        self.contrast_button = tk.Button(self.editor_window, text="Изменить констрастность", command=self.adjust_contrast)
        self.contrast_button.pack(pady=5)

        # Кнопка для изменения резкости
        self.sharpness_button = tk.Button(self.editor_window, text="Изменить резкость", command=self.adjust_sharpness)
        self.sharpness_button.pack(pady=5)

        # Кнопка для изменения масштаба
        self.scale_button = tk.Button(self.editor_window, text="Изменить масштаб", command=self.adjust_scale)
        self.scale_button.pack(pady=5)

        # Кнопка "Назад" для возврата на главный экран
        self.back_button = tk.Button(self.editor_window, text="Назад", command=self.go_back)
        self.back_button.pack(pady=5)

        # Кнопка "Анализ"
        self.analyze_button = tk.Button(self.editor_window, text="Анализ", command=self.analyze_image)
        self.analyze_button.pack(pady=5)

        # Отображаем изображение в редакторе
        self.update_editor_image()

    def update_editor_image(self):
        # Преобразуем изображение в формат, который может быть отображен в Tkinter
        self.tk_editor_image = ImageTk.PhotoImage(self.image)

        # Удаляем предыдущее изображение
        for widget in self.image_frame.winfo_children():
            widget.destroy()

        # Создаем метку для изображения
        self.editor_image_label = tk.Label(self.image_frame, image=self.tk_editor_image)
        self.editor_image_label.pack()

        # Обновляем размеры Canvas в соответствии с размером изображения
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def adjust_contrast(self):
        # Запрашиваем значение контрастности
        factor = simpledialog.askfloat("Контрастность", "Введите значение от 0.0 до 3.0:", minvalue=0.0, maxvalue=3.0)
        if factor is not None:
            enhancer = ImageEnhance.Contrast(self.image)
            self.image = enhancer.enhance(factor)
            self.update_editor_image()

    def adjust_sharpness(self):
        # Запрашиваем значение резкости
        factor = simpledialog.askfloat("Резкость", "Введите значение от 0.0 до 3.0:", minvalue=0.0, maxvalue=3.0)
        if factor is not None:
            enhancer = ImageEnhance.Sharpness(self.image)
            self.image = enhancer.enhance(factor)
            self.update_editor_image()

    def adjust_scale(self):
        # Запрашиваем новый размер масштаба
        scale = simpledialog.askfloat("Масштаб", "Введите значение от 0.1 до 10.0:", minvalue=0.1, maxvalue=10.0)
        if scale is not None:
            width, height = self.image.size
            new_size = (int(width * scale), int(height * scale))
            self.image = self.image.resize(new_size, Image.Resampling.LANCZOS)
            self.update_editor_image()

    def go_back(self):
        # Закрываем окно редактора и возвращаемся к главному окну
        self.editor_window.destroy()
        self.root.deiconify()

    def analyze_image(self):
        analyzer = ImageAnalyzer(self.image)
        analyzer.analyze_image()
