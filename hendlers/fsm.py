from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import buttons
from aiogram.types import ReplyKeyboardRemove
from db import db_main


class FSM_store(StatesGroup):
    name_products = State()
    size = State()
    category = State()
    price = State()
    product_id = State()
    photo_products = State()
    submit = State()


async def start_fsm(message: types.Message):
    await message.answer('Укажите название или бренд товара: ')
    await FSM_store.name_products.set()


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_products'] = message.text

    await message.answer('Введите размер товара: ')
    await FSM_store.next()


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await message.answer('Введите категорию товара: ')
    await FSM_store.next()


async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await message.answer('Введите цену товара: ')
    await FSM_store.next()


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await message.answer('Введите артикул (он должен быть уникальным): ')
    await FSM_store.next()


async def load_product_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_id'] = message.text

    await message.answer('Отправьте фото: ')
    await FSM_store.next()


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

        await message.answer_photo(
            photo=data['photo'],
            caption=f'Название/Бренд товара: {data["name_products"]}\n'
                    f'Размер товара: {data["size"]}\n'
                    f'Категория товара: {data["category"]}\n'
                    f'Стоимость: {data["price"]}\n'
                    f'Артикул: {data["product_id"]}\n',
            reply_markup=buttons.submit_button
        )
        await FSM_store.next()


async def submit(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardRemove()

    if message.text == 'Да':
        async with state.proxy() as data:
            await message.answer('Отлично, Данные в базе!', reply_markup=kb)
            await db_main.sql_insert_products(
                name_product=data['name_products'],
                size=data['size'],
                price=data['price'],
                product_id=data['product_id'],
                photo=data['photo']
            )
    elif message.text == 'Нет':
        await message.answer('Хорошо, регистрация завершено!')

    else:
        await state.finish()
        await message.answer('Выберите Да или Нет!!!')


def register_store(dp: Dispatcher):
    dp.register_message_handler(start_fsm, commands=['reg'])
    dp.register_message_handler(load_name, state=FSM_store.name_products)
    dp.register_message_handler(load_size, state=FSM_store.size)
    dp.register_message_handler(load_category, state=FSM_store.category)
    dp.register_message_handler(load_price, state=FSM_store.price)
    dp.register_message_handler(load_product_id, state=FSM_store.product_id)
    dp.register_message_handler(load_photo, state=FSM_store.photo_products,
                                content_types=['photo'])
    dp.register_message_handler(submit, state=FSM_store.submit)
