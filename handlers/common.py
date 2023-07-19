from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from API.facts_api import facts_api
from keyboards.inline import fact_inline_keyboard

common_router = Router()


@common_router.message(Command('start'))
async def handle_start(message: Message):
    await message.answer(
        'Привет! Выбери факт, который ты хочешь.',
        reply_markup=fact_inline_keyboard)


