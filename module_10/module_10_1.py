# Задача "Потоковая запись в файлы":
# Необходимо создать функцию write_words(word_count, file_name), где word_count - количество записываемых слов,
# file_name - название файла, куда будут записываться слова.
# Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием
# после записи каждого на 0.1 секунду.
# Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
# В конце работы функции вывести строку "Завершилась запись в файл <название файла>".
#
# После создания файла вызовите 4 раза функцию write_words, передав в неё следующие значения:
# 10, example1.txt
# 30, example2.txt
# 200, example3.txt
# 100, example4.txt
# После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
# 10, example5.txt
# 30, example6.txt
# 200, example7.txt
# 100, example8.txt
# Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
# Также измерьте время затраченное на выполнение функций и потоков. Как это сделать рассказано в лекции к домашнему заданию.
#
# Пример результата выполнения программы:
# Алгоритм работы кода:
# # Импорты необходимых модулей и функций
# # Объявление функции write_words
# # Взятие текущего времени
# # Запуск функций с аргументами из задачи
# # Взятие текущего времени
# # Вывод разницы начала и конца работы функций
# # Взятие текущего времени
# # Создание и запуск потоков с аргументами из задачи
# # Взятие текущего времени
# # Вывод разницы начала и конца работы потоков
# Вывод на консоль:
# Завершилась запись в файл example1.txt
# Завершилась запись в файл example2.txt
# Завершилась запись в файл example3.txt
# Завершилась запись в файл example4.txt
# Работа потоков 0:00:34.003411 # Может быть другое время
# Завершилась запись в файл example5.txt
# Завершилась запись в файл example6.txt
# Завершилась запись в файл example8.txt
# Завершилась запись в файл example7.txt
# Работа потоков 0:00:20.071575 # Может быть другое время
# Примечания:
# Не переживайте, если программа выполняется долго, учитывая кол-во слов,
# максимальное время выполнения в потоках не должно превышать ~20 секунд, а в функциях ~34 секунды.
# Cледует заметить, что запись в example8.txt завершилась раньше, чем в example7.txt, т.к. потоки работали почти одновременно.


import time    # Импорты необходимых модулей и функций
import threading

def write_words(word_count, file_name):    # Объявление функции write_words
    with open(file_name, 'w', encoding='utf-8') as file:
        for word in range(1, word_count + 1):
            file.write(f'Какое-то слово № {word}\n')
            time.sleep(0.1)
    print(f"Завершилась запись в файл: {file_name}")

start_time = time.time()    # Взятие текущего времени

write_words(10, "example1.txt")     # Запуск функций с аргументами из задачи
write_words(30, "example2.txt")
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time.time()      # Взятие текущего времени
print('Работа потоков: ', round(end_time - start_time, 6), 'сек')       # Вывод разницы начала и конца работы функций

time1 = time.time()     # Взятие текущего времени

flow1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))     # Создание и запуск потоков с аргументами из задачи
flow2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
flow3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
flow4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

flow1.start()
flow2.start()
flow3.start()
flow4.start()

flow1.join()
flow2.join()
flow3.join()
flow4.join()

time2 = time.time()     # Взятие текущего времени

print('Работа потоков: ', round(time2 - time1, 6), 'сек')   # Вывод разницы начала и конца работы потоков
