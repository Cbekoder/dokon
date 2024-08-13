from aiogram.types import CallbackQuery
from bot.loader import dp


@dp.callback_query(lambda callback: callback.data.startswith('set_lang'))
async def language_handler(callback: CallbackQuery):
    language_code = callback.data.split(':')[1]

    if language_code == 'uz':
        response_text = "You selected O'zbek 🇺🇿"
    elif language_code == 'ru':
        response_text = "Вы выбрали русский 🇷🇺"
    elif language_code == 'en':
        response_text = "You selected English 🇬🇧"
    else:
        response_text = ""
    await callback.message.answer(response_text)

    await callback.answer("You selected")
