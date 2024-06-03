from typing import Optional

from src.db.database import get_async_session
from src.crud import result_test_crud
from src.schemas import test_schemas


async def db_get_test_data_list(user_id: int) -> (
    Optional[test_schemas.ResultTestRead] | None
):
    async for session in get_async_session():
        user = await result_test_crud.crud_get_test_data_list(
            user_id=user_id,
            session=session
        )
        return user


async def db_get_test_data(test_id: int) -> (
    Optional[test_schemas.ResultTestRead] | None
):
    async for session in get_async_session():
        user = await result_test_crud.crud_get_test_data(
            test_id=test_id,
            session=session
        )
        return user


async def db_create_new_result_test(data: test_schemas.ResultTestCreate) -> (
    Optional[test_schemas.ResultTestRead] | None
):
    async for session in get_async_session():
        response = await result_test_crud.crud_create_new_result_test(
            data=data,
            session=session
        )
        return response
