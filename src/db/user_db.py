from typing import Optional, List

from src.db.database import get_async_session
from src.crud import user_crud
from src.schemas import user_schemas


async def db_get_user_data(user_id: int) -> (
    Optional[user_schemas.UserRead] | None
):
    async for session in get_async_session():
        user = await user_crud.crud_get_user_data(
            user_id=user_id,
            session=session
        )
        return user


async def db_get_users_data_list() -> (
    List[user_schemas.UserListRead] | None
):
    async for session in get_async_session():
        user = await user_crud.crud_get_users_data_list(
            session=session
        )
        return user


async def db_create_new_user(data: user_schemas.UserCreate) -> (
    Optional[user_schemas.UserRead] | None
):
    async for session in get_async_session():
        response = await user_crud.crud_create_new_user(
            data=data,
            session=session
        )
        return response
