from typing import Optional, List

from sqlalchemy import insert, select, func
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas import user_schemas
from src.models import user, result_test


async def crud_get_user_data(
    user_id: int,
    session: AsyncSession,

) -> Optional[user_schemas.UserRead]:
    query = (
        select(user.User).
        where(user.User.user_id == user_id)
    )
    result = await session.execute(query)
    data = result.scalar()
    return data


async def crud_get_users_data_list(
    session: AsyncSession,

) -> List[user_schemas.UserListRead]:
    query = (
        select(
            user.User.id,
            user.User.user_id,
            user.User.first_name,
            user.User.last_name,
            user.User.username,
            user.User.admin,
            func.count(result_test.ResultTest.id).label('result_test_count')
        )
        .outerjoin(
            result_test.ResultTest,
            user.User.user_id == result_test.ResultTest.user_id
        )
        .group_by(user.User.id)
    )
    result = await session.execute(query)
    data = result.all()
    return data


async def crud_create_new_user(
    data: user_schemas.UserCreate,
    session: AsyncSession,
):
    stmt = (
        insert(user.User).
        values(**data.model_dump())
    )
    await session.execute(stmt)
    await session.commit()
    return {"status": 201}
