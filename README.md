# Приложение для обработки фото

## Содержание

- [Краткое описание программы](#краткое_описание_программы)
- [Функционал](#функционал)
- [Интерфейс](#интерфейс)
- [Используемые библиотеки](#используемые_библиотеки)

## Краткое описание программы

Данное приложение позволит численно охарактеризовать объекты на фото: форма, количество, толщина, длина объектов. Предполагается, что в дальнейшем программа будет ориенирована на анализ снимков нанообъектов

## Функционал 

Пользователь сможет загружать снимки с объектами, обрабатывать их для корректного отображения (резкость, масштаб и контрастность) и получать информацию о них в отдельном окне, также будет возможность сохранить полученные данные в виде файла.

## Интерфейс

Интерфейс будет включать начальное окно с предложением загрузить изображение:

![1](https://github.com/user-attachments/assets/44dee994-38b9-47e7-b479-63c789df3852)

Затем появляется окно с возможностью редактирования исходного фото и дальнейшем анализом:

![21](https://github.com/user-attachments/assets/a6907bda-cccf-4aa6-80b6-9fc751644da5)

Окончательный вид представлен в виде таблицы с полученными данными и обработанным снимком, также у пользователя есть возможность скачать полученную информацию в виде файла и загрузить новое фото для обработки и анализа:

![3](https://github.com/user-attachments/assets/64f92325-17e5-425e-9775-d3d460390552)

## Используемые библиотеки

- scikit-image - для обработки и анализа снимков
- flet - для создания интерфейса
