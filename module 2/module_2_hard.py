# Дополнительное практическое задание по модулю: "Основные операторы"

# Задание "Слишком древний шифр"
# перед вами появились ворота (выход из ловушки) с двумя каменными вставками для чисел.
# В первом поле камни с числом менялись постоянно (от 3 до 20) случайным образом, а второе было всегда пустым.
# Во вторую вставку нужно написать те пары чисел друг за другом, чтобы число из первой вставки
# было кратно(делилось без остатка) сумме их значений.

# Пример кратности(деления без остатка):
# 1 + 2 = 3 (сумма пары)
# 9 / 3 = 3 (ровно 3 без остатка)
# 9 кратно 3 (9 делится на 3 без остатка)

# Пример 1:
# 9 - число из первой вставки
# 1218273645 - нужный пароль (1 и 2, 1 и 8, 2 и 7, 3 и 6, 4 и 5 - пары; число 9 кратно сумме каждой пары)
#
# Пример 2:
# 11 - число из первой вставки
# 11029384756 - нужный пароль (1 и 10, 2 и 9, 3 и 8, 4 и 7, 5 и 6 - пары; число 11 кратно сумме каждой пары)

# числа в первой вставке будут попадаться случайно
# *** воспользуемся библиотекой (import random)
# Составьте алгоритм, используя циклы, чтобы в независимости от введённого числа n (от 3 до 20)
# программа выдавала нужный пароль result, для одного введённого числа.

# Что является парой?:
# Пары являются уникальными на примере следущего:
# 7 3 3 5 8
# В этой последовательности уникальными парами являются:
# Для первой 7: 73 73 75 78
# Для второй 3: 33 35 38 (с пеервой 7 у этой 3 уже есть пара, поэтому её не берём).
#
# Все пароли для чисел от 3 до 20 (для сверки): # *** Создадим словарь passcode{key:pass}
# 3 - 12
# 4 - 13
# 5 - 1423
# 6 - 121524
# 7 - 162534
# 8 - 13172635
# 9 - 1218273645
# 10 - 141923283746
# 11 - 11029384756
# 12 - 12131511124210394857
# 13 - 112211310495867
# 14 - 1611325212343114105968
# 15 - 1214114232133124115106978
# 16 - 1317115262143531341251161079
# 17 - 11621531441351261171089
# 18 - 12151811724272163631545414513612711810
# 19 - 118217316415514613712811910
# 20 - 13141911923282183731746416515614713812911
#
#
# Примечания:
# Можно использовать как цикл for, так и цикл while
# Первое число не входит в одно из чисел пары,
# Пары чисел подбираются от 1 до 20 для текущего числа.

import random

n = random.randint(3, 20)
print(f'число из первой вставки: {n}')

def passwd(n):
    result = str()
    for i in range(1, n):
        for j in range(i+1, n):
            summ = i + j
            if n >= summ and n % summ == 0:
                result += str(i) + str(j)
    return(result)

print(f'пароль: {passwd(n)}')