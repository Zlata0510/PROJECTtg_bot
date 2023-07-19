from aiogram import Router, F
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.types import Message, CallbackQuery

from API.facts_api import facts_api

facts_router = Router()


@facts_router.callback_query()
async def handle_fact(query: CallbackQuery):
    fact = await facts_api.get_facts()
    await query.message.answer(fact)
