from aiogram import types, Dispatcher, executor
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import buttons
from aiogram.types import ReplyKeyboardRemove
from db import db_main

async def start(message: types.Message):
    await message.answer(text='Здравствуйте чем могу помочь?',
                         reply_markup=buttons.start)


async def info_bot(message: types.Message):
    await message.answer(text='Уважаемый пользователь, этот бот поможет вам подобрать лучший образ одежд на осень!')


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(info_bot, commands=['info'])
