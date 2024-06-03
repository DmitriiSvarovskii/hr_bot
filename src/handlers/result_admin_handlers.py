from aiogram import types, Router, F
from aiogram.exceptions import TelegramBadRequest

from src.lexicons import result_test_text
from src.keyboards import result_admin_test_kb as kb
from src.callbacks import result_test_cd
from src.db import result_test_db, user_db


router = Router(name=__name__)


@router.callback_query(F.data == 'press_result_employees')
async def process_of_pressing_empl_result(
    callback: types.CallbackQuery,
):
    users_data = await user_db.db_get_users_data_list()
    if users_data:
        keyboards = await kb.create_kb_result_users_list(
            users_data=users_data
        )
        await callback.message.edit_text(
            text=result_test_text.common_text['select_result_empl_test'],
            reply_markup=keyboards
        )
    else:
        await callback.answer(
            text=result_test_text.common_text['you_dont_have_test'],
            show_alert=True
        )


@router.callback_query(result_test_cd.ResultAdminTestCbData.filter())
async def process_select_employees(
    callback: types.CallbackQuery,
    callback_data: result_test_cd.ResultAdminTestCbData
):
    data = await result_test_db.db_get_test_data_list(
        user_id=callback_data.user_id
    )
    if data:
        keyboards = await kb.create_kb_result_test_admin_list(
            data=data,
            user_id=callback_data.user_id
        )
        await callback.message.edit_text(
            text=result_test_text.common_text['select_result_test'],
            reply_markup=keyboards
        )
    else:
        await callback.answer(
            text=result_test_text.common_text['empl_dont_have_test'],
            show_alert=True
        )


@router.callback_query(result_test_cd.ResultAdminListTestCbData.filter())
async def process_one_test_employees(
    callback: types.CallbackQuery,
    callback_data: result_test_cd.ResultAdminListTestCbData
):
    result_test_data = await result_test_db.db_get_test_data(
        test_id=callback_data.test_id
    )
    data = await result_test_db.db_get_test_data_list(
        user_id=callback_data.user_id
    )
    keyboards = await kb.create_kb_result_test_admin_list(
        data=data,
        user_id=callback_data.user_id
    )
    text = await result_test_text.generate_result_text(data=result_test_data)
    try:
        await callback.message.edit_text(text=text, reply_markup=keyboards)
    except TelegramBadRequest:
        await callback.answer(text="Повторный запрос")
