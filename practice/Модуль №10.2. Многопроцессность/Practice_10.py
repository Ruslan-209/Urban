import multiprocessing as mp  # Импорт модуля для работы с многопроцессностью
import datetime  # Импорт модуля для работы с датой и временем
from PIL import Image  # Импорт библиотеки для работы с изображениями
import os  # Импорт модуля для работы с операционной системой, например, для проверки существования файлов


# Функция для изменения размера изображений
def resize_image(image_paths, pipe, stop_event):
    for image_path in image_paths:  # Проход по всем путям изображений
        if os.path.exists(image_path):  # Проверка, существует ли файл
            image = Image.open(image_path)  # Открытие изображения
            image = image.resize((800, 600))  # Изменение размера изображения до 800x600 пикселей
            image.save(image_path)  # Сохранение изображения с новым размером
            pipe.send(image_path)  # Отправка пути к обработанному изображению в другой процесс через канал
    stop_event.set()  # Установка события для уведомления, что процесс завершен
    pipe.close()  # Закрытие канала после завершения работы


# Функция для изменения цвета изображений (конвертация в оттенки серого)
def change_color(pipe, stop_event):
    # Продолжаем работать, пока не установлено событие остановки и в канале есть данные
    while not stop_event.is_set() or pipe.poll():
        try:
            image_path = pipe.recv()  # Получение пути к изображению из канала
            image = Image.open(image_path)  # Открытие изображения
            image = image.convert('L')  # Преобразование изображения в оттенки серого (ч/б)
            image.save(image_path)  # Сохранение изображения с новым цветом
        except EOFError:  # Если в канале больше нет данных, выходим из цикла
            break
    pipe.close()  # Закрытие канала после завершения работы


if __name__ == '__main__':
    data = []  # Список для хранения путей к изображениям
    conn1, conn2 = mp.Pipe()  # Создание двухстороннего канала для общения между процессами
    stop_event = mp.Event()  # Создание события, которое будет сигнализировать о завершении процесса

    # Заполнение списка путями к изображениям
    for i in range(1, 10):
        data.append(f'./images/img_{i}.jpg')  # Путь к изображению формируется на основе номера

    # Создание процессов для изменения размера и изменения цвета изображений
    resize_process = mp.Process(target=resize_image, args=(data, conn1, stop_event))
    change_process = mp.Process(target=change_color, args=(conn2, stop_event))

    # Измерение времени начала выполнения программы
    start = datetime.datetime.now()
    resize_process.start()  # Запуск процесса изменения размера изображений
    change_process.start()  # Запуск процесса изменения цвета изображений

    # Ожидание завершения обоих процессов
    resize_process.join()
    change_process.join()

    # Измерение времени завершения программы
    end = datetime.datetime.now()

    # Вывод времени, затраченного на выполнение программы
    print("Execution time:", end - start)
