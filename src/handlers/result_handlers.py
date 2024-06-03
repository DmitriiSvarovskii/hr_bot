from aiogram import types, Router, F
from aiogram.exceptions import TelegramBadRequest

from src.lexicons import result_test_text
from src.keyboards import result_test_kb as kb
from src.callbacks import result_test_cd
from src.db import result_test_db, user_db


from src.keyboards import main_kb
from src.lexicons import text_main_menu


router = Router(name=__name__)


@router.callback_query(F.data == 'press_my_result')
async def process_of_pressing_my_result(
    callback: types.CallbackQuery,
):
    data = await result_test_db.db_get_test_data_list(
        user_id=callback.message.chat.id
    )
    if data:
        keyboards = await kb.create_kb_result_test_list(
            data=data
        )
        await callback.message.edit_text(
            text=result_test_text.common_text['select_result_test'],
            reply_markup=keyboards
        )
    else:
        await callback.answer(
            text=result_test_text.common_text['you_dont_have_test'],
            show_alert=True
        )


@router.callback_query(result_test_cd.ResultTestCbData.filter())
async def process_waiting_answer_to_question_1(
    callback: types.CallbackQuery,
    callback_data: result_test_cd.ResultTestCbData
):
    result_test_data = await result_test_db.db_get_test_data(
        test_id=callback_data.test_id
    )
    data = await result_test_db.db_get_test_data_list(
        user_id=callback.message.chat.id
    )
    keyboards = await kb.create_kb_result_test_list(
        data=data
    )
    text = await result_test_text.generate_result_text(data=result_test_data)
    try:
        await callback.message.edit_text(text=text, reply_markup=keyboards)
    except TelegramBadRequest:
        await callback.answer(text="Повторный запрос")


@router.callback_query(F.data == 'press_menu')
async def press_main_menu(callback: types.CallbackQuery):
    user_data = await user_db.db_get_user_data(
        user_id=callback.message.chat.id
    )
    keyboard = await main_kb.create_kb_main(
        admin=user_data.admin
    )
    await callback.message.edit_text(
        text=text_main_menu.main_menu_dict['start'],
        reply_markup=keyboard
    )
