from aiogram.types import Message
from typing import Optional

from src.schemas import user_schemas


async def create_user_data_from_message(
    message: Message
) -> Optional[user_schemas.UserCreate]:
    user_data = user_schemas.UserCreate(
        user_id=message.from_user.id,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        username=message.from_user.username
    )
    return user_data
