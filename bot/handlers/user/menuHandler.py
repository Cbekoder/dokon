# bot/handlers/user/menuHandler.py
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from bot.keyboards.default.menuKeyboard import menuKeyboard, bolimlar
from bot.keyboards.inline.oziq_ovaqtlar import foods, meats
from loader import dp

@dp.message(Command('menu'))
async def start_menu_handler(message: Message):
    await message.reply("Menuni tanlash", reply_markup=menuKeyboard)


@dp.message(lambda message: message.text == "Bo'limlar📁")
async def BolimHandler(message: Message):
    await message.delete()
    await message.answer("Quyidagi bo'limlar mavjud: ", reply_markup=bolimlar)

@dp.message(lambda message: message.text == "Oziq-ovqat")
async def foodsHandler(message: Message):
    await message.answer("Quyidagi bo'limlar mavjud: ", reply_markup=foods)


@dp.callback_query(lambda callback: callback.data.startswith('product'))
async def language_handler(callback: CallbackQuery):
    catergory = callback.data.split(":")[1]

    if catergory == "meat":
        await callback.message.edit_text("Qaysi turdagi go'sht mahsuloti kerak:", reply_markup=meats)
