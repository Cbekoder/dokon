
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

foods = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text="Go'sht mahsulotlar", callback_data='product:meat'),
        InlineKeyboardButton(text="Sut mahsulotlar", callback_data='product:milk'),
        InlineKeyboardButton(text="Non mahsulotlar", callback_data='product:bread'),
        InlineKeyboardButton(text="Shirinliklar mahsulotlar", callback_data='product:sweet')
        ]
    ]
)

meats = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text="Mol go'shti", callback_data='meat:mol'),
        InlineKeyboardButton(text="Qo'y go'shti", callback_data='meat:qoy'),
        InlineKeyboardButton(text="Tovuq go'shti", callback_data='meat:tovuq'),
        InlineKeyboardButton(text="Baliq go'shti", callback_data='meat:baliq')
        ]
    ]
)