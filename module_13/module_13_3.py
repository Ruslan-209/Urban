# Задача "Он мне ответил!":
# Измените функции start и all_messages так, чтобы вместо вывода в консоль строки отправлялись в чате телеграм.
# Запустите ваш Telegram-бот и проверьте его на работоспособность.
# Пример результата выполнения программы:
#
# Примечания:
# Для ответа на сообщение запускайте метод answer асинхронно.
# При отправке вашего кода на GitHub не забудьте убрать ключ для подключения к вашему боту!

from aiogram import Bot, Dispatcher, executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ''
bot = Bot(token= api)
dp = Dispatcher(bot, storage= MemoryStorage())

@dp.message_handler(commands= ['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Привет! Я бот помогающий твоему здоровью.')
    # await message.answer(message.text)

@dp.message_handler()
async def all_massages(message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')
    # await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)