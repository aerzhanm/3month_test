import sqlite3
from db import queries

db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()


async def sql_create():
    if db:
        print('База данных подключена!')

    cursor.execute(queries.CREATE_TABLE_PRODUCTS)
    cursor.execute(queries.CREATE_ORDER_TABLE)
    db.commit()


async def sql_insert_products(name_product, size, price, product_id, photo):
    with sqlite3.connect('db/store.sqlite3') as db_with:
        cursor_with = db_with.cursor()
        cursor_with.execute(queries.INSERT_PRODUCTS_QUERY, (
            name_product,
            size,
            price,
            product_id,
            photo
        ))
        db_with.commit()


async def sql_order_products(size, product_id, amount_products, phone_number):
    with sqlite3.connect('db/store.sqlite3') as db_with:
        cursor_with = db_with.cursor()
        cursor_with.execute(queries.INSERT_ORDER_PRODUCTS, (
            size,
            product_id,
            amount_products,
            phone_number
        ))
        db_with.commit()


