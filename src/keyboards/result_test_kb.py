from typing import List

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import (
    InlineKeyboardButton,
)

from src.lexicons import text_main_menu
from src.schemas import test_schemas
from src.callbacks import result_test_cd


async def create_kb_result_test_list(
    data: List[test_schemas.ResultTestRead]
):
    keyboard = InlineKeyboardBuilder()

    for result_test in data:
        keyboard.row(
            InlineKeyboardButton(
                text=f"Тест от {result_test.created_at.strftime('%d.%m.%Y')}",
                callback_data=result_test_cd.ResultTestCbData(
                    test_id=result_test.id,
                ).pack()))

    back_button = [InlineKeyboardButton(
        text=value['text'],
        callback_data=value['callback_data']
    ) for value in text_main_menu.back_button_dict.values()]

    keyboard.row(*back_button, width=1)

    return keyboard.as_markup()
