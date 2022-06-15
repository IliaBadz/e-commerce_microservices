import os

from project.db.models.consumer import Consumer

import motor.motor_asyncio
from pydantic import EmailStr
from beanie import init_beanie, PydanticObjectId


class ConsumerDB:
    """Initialize database and implement CRUD operations"""

    def __init__(self):
        self._host_port = os.getenv('MONGODB_HOST_PORT')
        self.client = None
        self.db = None

    async def initialize_db(self):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(self._host_port)
        self.db = self.client.test
        await init_beanie(database=self.db, document_models=[Consumer])

    async def create_user(self,
                          username,
                          full_name,
                          email,
                          hashed_password,
                          created_at,
                          is_active,
                          is_verified):
        """Add new consumer if it is not already in database."""
        consumer = Consumer(username=username,
                            full_name=full_name,
                            email=email,
                            hashed_password=hashed_password,
                            created_at=created_at,
                            is_active=is_active,
                            is_verified=is_verified)

        await consumer.insert()

        consumer = await self.get_user_by_username(username=username)

        return consumer

    async def get_user_by_id(self, user_id):
        consumer = await Consumer.get(PydanticObjectId(user_id))
        return consumer

    async def get_user_by_username(self, username: str):
        consumer = await Consumer.find_one(Consumer.username == username)
        return consumer

    async def update_user(self, username: str, full_name: str, email: EmailStr):
        consumer_in_db = await self.get_user_by_username(username)

        await consumer_in_db.set({Consumer.full_name: full_name,
                                  Consumer.email: email})

        updated_consumer = await self.get_user_by_username(username)

        return updated_consumer

    async def update_status(self, username: str, is_active: bool, is_verified: bool):
        consumer_in_db = await self.get_user_by_username(username)
        await consumer_in_db.set({Consumer.is_active: is_active,
                                  Consumer.is_verified: is_verified})

        updated_consumer = await self.get_user_by_username(username)
        return updated_consumer
