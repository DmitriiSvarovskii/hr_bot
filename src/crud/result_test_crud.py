from typing import Optional, List

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas import test_schemas
from src.models import result_test


async def crud_get_test_data_list(
    user_id: int,
    session: AsyncSession,

) -> List[test_schemas.ResultTestRead]:
    query = (
        select(result_test.ResultTest).
        where(result_test.ResultTest.user_id == user_id)
    )
    result = await session.execute(query)
    data = result.scalars().all()
    return data


async def crud_get_test_data(
    test_id: int,
    session: AsyncSession,

) -> Optional[test_schemas.ResultTestRead]:
    query = (
        select(result_test.ResultTest).
        where(result_test.ResultTest.id == test_id)
    )
    result = await session.execute(query)
    data = result.scalar()
    return data


async def crud_create_new_result_test(
    data: test_schemas.ResultTestCreate,
    session: AsyncSession,
):
    stmt = (
        insert(result_test.ResultTest).
        values(**data.model_dump())
    )
    await session.execute(stmt)
    await session.commit()
    return {"status": 201}
