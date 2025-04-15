# bot/handlers/admin.py

from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("add_product"))
async def add_product_handler(message: types.Message):
    await message.answer("لطفا اطلاعات محصول را وارد کنید.")
