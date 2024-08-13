from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup
from aiogram import html
from keyboards.inline.language_choice import send_language

from loader import dp

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Salom, {html.bold(message.from_user.full_name)}!\nQuyidagilar orqali tilni tanlang: ", reply_markup=send_language)
