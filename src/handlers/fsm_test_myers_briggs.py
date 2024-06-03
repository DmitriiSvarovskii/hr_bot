from aiogram import types, Router, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext

from src.db import user_db, result_test_db
from src.lexicons import text_main_menu, questions, answers, result_test_text
from src.keyboards import main_kb, kb_test_myers_briggs as kb
from src.state import FSMMyersBriggs
from src.schemas import test_schemas
from src.utils.calculate import calculate_scores


router = Router(name=__name__)


@router.callback_query(F.data == 'press_start_test')
async def process_waiting_answer_to_question_1(
    callback: types.CallbackQuery,
    state: FSMContext
):
    if callback.message:
        try:
            await callback.message.delete()
        except TelegramBadRequest:
            pass
    await callback.message.answer(
        text=result_test_text.common_text['start_text'],
        reply_markup=kb.create_kb_answer()
    )
    await callback.message.answer(
        text=questions.questions['question_1'],
        reply_markup=kb.create_kb_answer()
    )
    await state.set_state(FSMMyersBriggs.question_1)


@router.message(F.text == answers.answers['cancel'])
async def process_cancel_command_state_order(
    message: types.Message,
    state: FSMContext
):
    user_data = await user_db.db_get_user_data(
        user_id=message.chat.id
    )
    keyboard = await main_kb.create_kb_main(
        admin=user_data.admin
    )
    await message.answer(
        text=result_test_text.common_text['cancel_text'],
        reply_markup=types.ReplyKeyboardRemove()
    )
    await message.answer(
        text=result_test_text.common_text['select_item'],
        reply_markup=keyboard
    )
    await state.clear()


async def process_question_answer(
    message: types.Message,
    state: FSMContext
):
    question_number = int((await state.get_state()).split('_')[-1])
    await state.update_data({f"question_{question_number}": message.text})
    next_question_number = question_number + \
        1
    if next_question_number <= len(questions.questions):
        await message.answer(
            text=questions.questions[f'question_{next_question_number}'],
            reply_markup=kb.create_kb_answer()
        )
        await state.set_state(
            getattr(FSMMyersBriggs, f"question_{next_question_number}")
        )
    else:
        data = await state.get_data()
        data_test = calculate_scores(data)
        result_test_data = test_schemas.ResultTestCreate(
            user_id=message.chat.id,
            **data_test)
        await result_test_db.db_create_new_result_test(data=result_test_data)
        result_text = await result_test_text.generate_result_finish_test(
            data=result_test_data
        )
        await message.answer(
            text=result_text,
            reply_markup=types.ReplyKeyboardRemove()
        )
        user_data = await user_db.db_get_user_data(
            user_id=message.chat.id
        )
        keyboard = await main_kb.create_kb_main(
            admin=user_data.admin
        )
        await message.answer(
            text=text_main_menu.main_menu_dict['start'],
            reply_markup=keyboard
        )
        await state.clear()


for i in range(1, len(questions.questions) + 1):
    router.message.register(
        process_question_answer,
        getattr(FSMMyersBriggs, f"question_{i}"),
        (F.text == answers.answers['a']) | (F.text == answers.answers['b'])
    )
