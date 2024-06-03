from sqlalchemy import BIGINT, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING, List

from src.db.database import (
    Base, intpk, created_at
)

if TYPE_CHECKING:
    from .result_test import ResultTest


class User(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(BIGINT, unique=True)
    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    username: Mapped[str | None]
    admin: Mapped[bool] = mapped_column(server_default=text("false"))
    is_active: Mapped[bool] = mapped_column(server_default=text("true"))
    created_at: Mapped[created_at]

    result_tests: Mapped[List['ResultTest']
                         ] = relationship(back_populates="users")
