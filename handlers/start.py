from aiogram import types
from aiogram.dispatcher import Dispatcher

# Функция, которую подключим из bot.py
def register_start_handler(dp: Dispatcher):
    @dp.message_handler(commands=['start'])
    async def start_cmd(message: types.Message):
        await message.answer(
            "Привет! Это UniFinder.\n"
            "Введи название университета, и я покажу информацию!"
        )
