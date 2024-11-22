# Задание:
# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого объекта,
# чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.
#
# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
#   - Тип объекта.
#   - Атрибуты объекта.
#   - Методы объекта.
#   - Модуль, к которому объект принадлежит.
#   - Другие интересные свойства объекта, учитывая его тип (по желанию).
#
#
# Пример работы:
# number_info = introspection_info(42)
# print(number_info)
#
# Вывод на консоль:
# {'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}
#
# Рекомендуется создавать свой класс и объект для лучшего понимания
from pprint import pprint


def introspection_info(obj):
    return {'Тип объекта': type(obj).__name__,
            'Атрибуты объекта' : [attr for attr in dir(obj) if not callable(getattr(obj, attr))
                           and not attr.startswith("__")],
            'Методы объекта' : [method for method in dir(obj) if callable(getattr(obj, method))],
            'Модуль' : obj.__module__
            }

class ExampleClass:
    def __init__(self, value):
        self.value = value

    def method(self):
        return self.value

number_info = introspection_info(ExampleClass(42))
pprint(number_info)