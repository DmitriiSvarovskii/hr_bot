from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.lexicons import text_main_menu


async def create_kb_main(admin: bool) -> InlineKeyboardBuilder:
    keyboard = InlineKeyboardBuilder()

    buttons = []

    for key, value in text_main_menu.main_btn.items():
        if 'result_employees' in key and not admin:
            continue
        if 'callback_data' in value:
            button = InlineKeyboardButton(
                text=value['text'], callback_data=value['callback_data'])
        buttons.append(button)

    keyboard.row(*buttons, width=1)

    return keyboard.as_markup()
