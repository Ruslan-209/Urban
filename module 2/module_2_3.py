# Дан список чисел [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# Нужно выписывать из этого списка только положительные числа до тех пор, пока не встретите отрицательное или не закончится список (выход за границу).
# Пункты задачи:
# 1. Запишите исходный список в переменную my_list.
# 2. Напишите цикл while с соответствующими задаче условиями.
# 3. Используйте операторы прерывания/продолжения цикла в соответствии с условиями задачи.


my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):
    number = my_list[index]
    index += 1
    if number == 0:
        continue
    elif number >= 0:
        print(number)
    elif number < 0:
        break