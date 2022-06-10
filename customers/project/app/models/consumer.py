from datetime import date

from pydantic import EmailStr
from beanie import Document


class Consumer(Document):
    username: str
    full_name: str
    email: EmailStr
    hashed_password: str
    created_at: str
    is_active: bool = False
    is_verified: bool = False


class ConsumerOut(Document):
    username: str
    email: EmailStr
    created_at: date
