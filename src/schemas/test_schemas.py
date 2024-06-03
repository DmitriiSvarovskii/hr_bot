from datetime import datetime
from pydantic import BaseModel, ConfigDict


class ResultTestBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    e: int
    i: int
    s: int
    n: int
    t: int
    f: int
    j: int
    p: int


class ResultTestCreate(ResultTestBase):
    user_id: int


class ResultTestRead(ResultTestCreate):
    id: int
    created_at: datetime
