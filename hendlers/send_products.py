import sqlite3
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text



def get_db_connection():
    conn = sqlite3.connect('db/store.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn

async def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute('''
    SELECT * FROM products p 
    INNER JOIN products_details_pd ON p.product_id = pd.product id''').fetchall()
    conn.close()
    return products

async def start_sending_products(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    show_all_products = InlineKeyboardButton(text="Посмотреть",
                                             callback_data="show_all")
    keyboard.add(show_all_products)

    await message.answer(text="Нажми на кнопку чтобы посмотреть тавары:",
                         reply_markup=keyboard)

async def send_all_products(callback_query: types.CallbackQuery):
    products = fetch_all_products()

    if products:
        for product in products:
            caption = (f'Название тавара - {product["name_product"]}\n'
                       f'Артикул - {product["product_id"]}\n'
                       f'Категория - {product["category"]}\n'
                       f"Размер - {product['size']}\n"
                       f"Цена - {product['price']} сом\n")
            await callback_query.message.answer_photo(photo=products['photo'],
                                                caption=caption)
    else:
        await callback_query.message.answer("Тавары не найдены!")






def register_send_products(dp: Dispatcher):
    dp.register_message_handler(start_sending_products, commands=['products'])
    dp.register_message_handler(send_all_products, Text(equals='show_all_products'))