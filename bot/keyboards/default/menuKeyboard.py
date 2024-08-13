# bot/keyboards/default/menuKeyboard.py

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuKeyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Bo'limlar📁"),
            KeyboardButton(text="Mahsulotlar📦")
        ],
        [
            KeyboardButton(text="Joylashuv📍", request_location=True)
        ]
    ]
)

bolimlar = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Oziq-ovqat"),
            KeyboardButton(text="Mevalar"),
            KeyboardButton(text="Sport anjomlari"),
            KeyboardButton(text="Kiyimlar"),
        ]
    ]
)
