from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



submit_button = ReplyKeyboardMarkup(resize_keyboard=True,
                                 row_width=2).add(
    KeyboardButton(text='Да'),
    KeyboardButton(text='Нет')
)

start = ReplyKeyboardMarkup(resize_keyboard=True,
                            row_width=2)

reg_buttons = KeyboardButton('/reg')
order_buttons = KeyboardButton('/order')
info_all_buttons = KeyboardButton('/info')


start.add(reg_buttons, order_buttons, info_all_buttons,
          )