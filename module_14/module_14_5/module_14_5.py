
from aiogram import Bot, Dispatcher, executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import logging
from crud_functions import *

logging.basicConfig(level= logging.INFO)
api = '7712655756:AAE1AvJF7XkkyLTaP9TgM2w56YXh-WKXV6s'
bot = Bot(token= api)
dp = Dispatcher(bot, storage= MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text= 'Информация')
button2 = KeyboardButton(text= 'Рассчитать')
button5 = KeyboardButton(text= 'Купить')
button6 = KeyboardButton(text='Регистрация')
kb.add(button, button2)
kb.add(button5)
kb.add(button6)

kb2 =  InlineKeyboardMarkup()
button3 = InlineKeyboardButton(text= 'Рассчитать норму калорий', callback_data= 'calories')
button4 = InlineKeyboardButton(text= 'Формулы расчёта', callback_data='formulas')


catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text= 'Product1', callback_data='product_buying'),
        InlineKeyboardButton(text='Product2', callback_data='product_buying'),
        InlineKeyboardButton(text='Product3', callback_data='product_buying'),
        InlineKeyboardButton(text='Product4', callback_data='product_buying')]
    ], resize_keyboard=True
)
kb2.add(button3, button4)

initiate_db()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000

@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    username = message.text
    if is_included(username):
        await message.answer("Пользователь существует, введите другое имя:")
    else:
        await state.update_data(username=username)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    email = message.text
    await state.update_data(email=email)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await message.answer("Регистрация прошла успешно", reply_markup=kb)
    await state.finish()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands= ['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    products = get_all_products()
    for product in products:
        id_, title, description, price = product
        with open(f'{id_}.JPG', 'rb') as img:
            await message.answer_photo(img)
        await message.answer(f'Название: {title} | Описание: {description} | Цена: {price}')
    await message.answer("Выберите продукт для покупки:", reply_markup=catalog_kb)

@dp.callback_query_handler(text= 'product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

@dp.message_handler(text= 'Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup=kb2)

@dp.callback_query_handler(text= 'formulas')
async def get_formulas(call):
    await call.message.answer(f'Для женщин: 10 х вес(кг) + 6,25 x рост(см) – 5 х возраст(г) - 161 \nДля мужчин: '
                              f'10 х вес(кг) + 6,25 x рост(см) – 5 х возраст(г) + 5')
    await call.answer()

@dp.message_handler(text= 'Информация')
async def info(message):
    await message.answer('Информация')

@dp.callback_query_handler(text= 'calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state= UserState.age)
async def set_growth(message, state):
    await state.update_data(age= int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state= UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth= int(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state= UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight= int(message.text))
    data = await state.get_data()
    await message.answer(f'Расчет калорийности по формуле Миффлина-Сан Жеора:'
                         f'\n1) для женщин: {10 * data["weight"] +6.25 * data["growth"] - 5 * data["age"] - 161} калорий '
                         f'\n2) для мужчин: {10 * data["weight"] +6.25 * data["growth"] - 5 * data["age"] + 5} калорий'
                         )
    await state.finish()

@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)