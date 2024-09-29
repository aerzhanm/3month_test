from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import buttons
from aiogram.types import ReplyKeyboardRemove
from db import db_main
from aiogram import types, Dispatcher


class FSM_order(StatesGroup):
    size = State()
    product_id = State()
    amount_products = State()
    phone_number = State()
    photo = State()
    submit = State()


async def start_order(message: types.Message):
    await message.answer('укажите размер тавара:')
    await FSM_order.next()


async def size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await message.answer('укажите категорию тавара:')
    await FSM_order.next()


async def product_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_id'] = message.text

    await message.answer('укажите количество тавара:')
    await FSM_order.next()


async def amount_products(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['amount'] = message.text

    await message.answer('укажите номер телефона:')
    await FSM_order.next()


async def phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text

    await message.answer('отправьте фото продукта:')
    await FSM_order.next()


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

        await message.answer_photo(
            photo=['photo'],
            caption=f'размер: {data["size"]}\n'
                    f'артикул: {data["product_id"]}\n'
                    f'количество: {data["amount"]}\n'
                    f'номер телефона: {data["phone_number"]}',
            reply_markup=buttons.submit_button
        )

        await FSM_order.next()


async def submit(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardRemove()

    if message.text == 'Да':
        async with state.proxy() as data:
            await message.answer('Отлично, Данные в базе!', reply_markup=kb)
            await db_main.sql_order_products(
                size=data['size'],
                product_id=data['product_id'],
                amount_products=data['amount_products'],
                phone_number=data['phone_number']
            )
    elif message.text == 'Нет':
        await message.answer('Хорошо, заказ завершен!')

    else:
        await state.finish()
        await message.answer('Выберите Да или Нет!!!')


def register_orders(dp: Dispatcher):
    dp.register_message_handler(start_order, commands=['order'])
    dp.register_message_handler(size, state=FSM_order.size)
    dp.register_message_handler(product_id, state=FSM_order.product_id)
    dp.register_message_handler(amount_products, state=FSM_order.amount_products)
    dp.register_message_handler(phone_number, state=FSM_order.phone_number)
    dp.register_message_handler(load_photo, state=FSM_order.photo)
    dp.register_message_handler(submit, state=FSM_order.submit)
