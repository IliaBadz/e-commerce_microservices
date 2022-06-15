from datetime import date

from pydantic import EmailStr
from beanie import Document, Indexed


class Consumer(Document):
    username: Indexed(str, unique=True)
    full_name: str
    email: Indexed(EmailStr, unique=True)
    hashed_password: str
    created_at: str
    is_active: bool = False
    is_verified: bool = False


class ConsumerOut(Document):
    username: str
    email: EmailStr
    created_at: date
