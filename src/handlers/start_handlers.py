from aiogram import Router, types
from aiogram.filters import CommandStart

from src.db import user_db
from src.utils import user_utils
from src.keyboards import main_kb
from src.lexicons import text_main_menu


router = Router(name=__name__)


@router.message(CommandStart())
async def process_start_command(message: types.Message):
    if message.chat.type == 'private':

        user_data = await user_db.db_get_user_data(
            user_id=message.chat.id
        )
        if not user_data:
            data = await user_utils.create_user_data_from_message(
                message=message
            )
            await user_db.db_create_new_user(
                data=data
            )
            keyboard = await main_kb.create_kb_main(admin=False)
            await message.answer(
                text=text_main_menu.main_menu_dict['start'],
                reply_markup=keyboard
            )
        if user_data:
            keyboard = await main_kb.create_kb_main(
                admin=user_data.admin
            )
            text = text_main_menu.main_menu_dict['start']
            if user_data.admin:
                text = text_main_menu.main_menu_dict['start_admin']
            await message.answer(
                text=text,
                reply_markup=keyboard
            )
    else:
        await message.reply(
            text=text_main_menu.main_menu_dict['error_private_chat']
        )
