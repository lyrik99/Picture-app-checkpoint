import tkinter as tk
from tkinter import filedialog, simpledialog
from PIL import Image, ImageTk
from image_editor import ImageEditor

class ImageLoaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Loader")

        # Кнопка для загрузки изображения
        self.load_button = tk.Button(root, text="Загрузите снимок", command=self.load_image)
        self.load_button.pack(pady=20)

        # Кнопка для подтверждения выбора изображения
        self.confirm_button = tk.Button(root, text="Далее", command=self.open_editor_window, state=tk.DISABLED)
        self.confirm_button.pack(pady=20)

        # Метка для отображения изображения
        self.image_label = tk.Label(root)
        self.image_label.pack()

    def load_image(self):
        # Открываем диалог для выбора файла
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.tif")])

        if file_path:
            # Загружаем изображение
            self.image = Image.open(file_path)

            # Преобразуем изображение в формат, который
            self.image.thumbnail((400, 400))

            # Изменяем размер изображения для предварительного просмотра
            self.tk_image = ImageTk.PhotoImage(self.image)

            # Обновляем метку для отображения изображения
            self.image_label.config(image=self.tk_image)
            self.image_label.image = self.tk_image

            # Включаем кнопку подтверждения
            self.confirm_button.config(state=tk.NORMAL)

    def open_editor_window(self):
        # Закрываем главное окно
        self.root.withdraw()

        # Открываем новое всплывающее окно
        self.editor = ImageEditor(self.image, self.root)
        self.editor.open_editor_window()
