# bot/handlers/user.py

from aiogram import Router, types, F
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("سلام! به ربات خوش اومدی.")
