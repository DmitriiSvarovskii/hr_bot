from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from src.db.database import (
    Base, intpk, created_at
)

if TYPE_CHECKING:
    from .user import User


class ResultTest(Base):
    __tablename__ = "result_tests"

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.user_id",
            ondelete="CASCADE"
        )
    )
    e: Mapped[int]
    i: Mapped[int]
    s: Mapped[int]
    n: Mapped[int]
    t: Mapped[int]
    f: Mapped[int]
    j: Mapped[int]
    p: Mapped[int]
    created_at: Mapped[created_at]

    users: Mapped['User'] = relationship(back_populates="result_tests")
