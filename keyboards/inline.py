from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardButton

random_fact_inline_button = InlineKeyboardButton(
    text='Случайный факт',
    callback_data='random_fact'
)

today_fact_inline_button = InlineKeyboardButton(
    text='Факт дня',
    callback_data='today_fact'
)

fact_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [random_fact_inline_button, today_fact_inline_button]
])
