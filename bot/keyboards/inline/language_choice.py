from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


builder = InlineKeyboardBuilder()

builder.button(text="O'zbek 🇺🇿", callback_data="set_lang:uz")
builder.button(text="Russian 🇷🇺", callback_data="set_lang:ru")
builder.button(text="English 🇬🇧", callback_data="set_lang:en")

send_language = InlineKeyboardMarkup(inline_keyboard=builder.export())
