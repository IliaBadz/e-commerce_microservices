from typing import Union
from datetime import datetime

from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    username: str
    full_name: Union[str, None] = None
    email: Union[EmailStr, None] = None
    password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = False
    is_verified: bool = False


class UpdateUser(BaseModel):
    full_name: str
    email: EmailStr


class UserInDB(User):
    hashed_password: str


class UserOut(User):
    id: str
