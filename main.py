import logging
from config import bot, dp, admin
from hendlers import echo, commands, fsm, send_products, zakaz_product
from aiogram.utils import executor
from db import db_main, queries

async def on_startup(_):
    for i in admin:
        await bot.send_message(chat_id=i, text="Бот включен!")
        await db_main.sql_create()
commands.register_commands(dp)
fsm.register_store(dp)
send_products.register_send_products(dp)
zakaz_product.register_orders(dp)


echo.register_echo(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
