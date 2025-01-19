from django.db import models

# Create your models here.


class Buyer(models.Model):                                          #  Модель покупателя

    name = models.CharField(max_length=100)                         # Имя покупателя
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # Баланс (10 цифр, 2 знака после запятой)
    age = models.PositiveIntegerField()                                     # Возраст (Только целые числа)

    def __str__(self):                       # Метод для строкового представления объекта
        return self.name                     # Возвращаем имя покупателя

class Game(models.Model):                                           #  Модель игры

    title = models.CharField(max_length=100)                        # Название игры (100 символов)
    cost = models.DecimalField(max_digits=10, decimal_places=2)     # Цена (10 цифр, 2 знака после запятой)
    size = models.DecimalField(max_digits=10, decimal_places=2)     # Размер файлов игры
    description = models.TextField()                                # Описание (неограниченное количество символов)
    age_limited = models.BooleanField(default=False)                # Ограничение возраста 18+
    buyer = models.ManyToManyField(Buyer)     # Покупатель обладающий игрой

    def __str__(self):                       # Метод для строкового представления объекта
        return self.title                    # Возвращаем название игры

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)  # Дата и время добавления

    def __str__(self):
        return self.title

"""
python manage.py makemigrations --Создание миграций для новых моделей

python manage.py migrate --Применение миграций к db.sqlite3
"""

"""
----------  Список QuerySet запросов в порядке вызовов ----------

python manage.py shell - Вход в консоль запросов QuerySet

from task1.models import Buyer, Game  - Импорт моделей Buyer и Game

-----  Открытие в Buyer объектов Ilia, Terminator2000, Ubivator432 ----------

Buyer.objects.create(name='Ilia', balance=1500.05, age=24)
Buyer.objects.create(name='Terminator2000', balance=42.15, age=52)
Buyer.objects.create(name='Ubivator432', balance=0.5 ,age=16) 

-----  Открытие в Game объектов Cyberpunk2077, Mario, Hitman  --------------

Game.objects.create(title='Cyberpunk2077', cost=31, size=46.2, description='Game of the year', age_limited=True)
Game.objects.create(title='Mario', cost=5, size=0.5, description='Old game', age_limited=False)  
Game.objects.create(title='Hitman', cost=12, size=36.6, description='Who kills Mark?', age_limited=True) 

-----  Сохранение покупателей в переменных  -----------

b1 = Buyer.objects.get(id=1)
b2 = Buyer.objects.get(id=2)
b3 = Buyer.objects.get(id=3)    < 18 лет

-----  Сохранение игр в переменных  -----------

g1 = Game.objects.get(id=1)      Ограничение до 18 лет
g2 = Game.objects.get(id=2)
g3 = Game.objects.get(id=3)      Ограничение до 18 лет

-----  Связывание объектов с полем buyer у записей Game

g1.buyer.set([b1, b2])  - Первой игрой владеют Ilia(b1) и Terminator2000(b2)
g2.buyer.set([b1, b3])  - Второй игрой владеют Ilia(b1) и Terminator2000(b2) и Ubivator432(b3)
g3.buyer.set([b1, b2])  - Третьей игрой владеет Ilia(b1)

"""
