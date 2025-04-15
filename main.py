# bot/main.py

import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import user, admin


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # ثبت روترها
    dp.include_router(user.router)
    dp.include_router(admin.router)

    # شروع ربات
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
