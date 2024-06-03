from typing import List

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import (
    InlineKeyboardButton,
)

from src.lexicons import text_main_menu
from src.schemas import user_schemas, test_schemas
from src.callbacks import result_test_cd


async def create_kb_result_users_list(
    users_data: List[user_schemas.UserListRead]
):
    keyboard = InlineKeyboardBuilder()

    for users in users_data:
        print(users)
        keyboard.row(
            InlineKeyboardButton(
                text=(
                    f"{users.first_name} {users.last_name}, "
                    f"всего тестов ({users.result_test_count})"
                ),
                callback_data=result_test_cd.ResultAdminTestCbData(
                    user_id=users.user_id
                ).pack()))

    back_button = [InlineKeyboardButton(
        text=value['text'],
        callback_data=value['callback_data']
    ) for value in text_main_menu.back_button_dict.values()]

    keyboard.row(*back_button, width=1)

    return keyboard.as_markup()


async def create_kb_result_test_admin_list(
    data: List[test_schemas.ResultTestRead],
    user_id: int
):
    keyboard = InlineKeyboardBuilder()

    for result_test in data:
        keyboard.row(
            InlineKeyboardButton(
                text=f"Тест от {result_test.created_at.strftime('%d.%m.%Y')}",
                callback_data=result_test_cd.ResultAdminListTestCbData(
                    test_id=result_test.id,
                    user_id=user_id
                ).pack()))

    back_button = [InlineKeyboardButton(
        text=value['text'],
        callback_data=value['callback_data']
    ) for value in text_main_menu.back_button_admin_dict.values()]

    keyboard.row(*back_button, width=1)

    return keyboard.as_markup()
