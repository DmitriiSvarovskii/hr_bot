from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from .test_schemas import ResultTestRead


class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None
    admin: Optional[bool] = False


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserRead(UserBase):
    id: int


class UserListRead(UserRead):
    result_test_count: int
