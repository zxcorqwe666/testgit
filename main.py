import asyncio
from aiogram import Dispatcher, Bot, types, F
from aiogram.filters import Command, CommandStart

Token = '6155823685:AAGZxwVWQCeUqJqkJge-kB_ZOrCw6vwA2A8'
bot = Bot(token=Token)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer('Hello')
async def main():
    await dp.start_polling(bot)

asyncio.run(main())