from project.db.consumer_db import ConsumerDB
from project.grpc.proto import consumer_pb2_grpc
from project.grpc.proto.consumer_pb2 import (Consumer, ConsumerOut, ConsumerStatus,
                                             UpdateStatus, UpdateConsumer, ConsumerUserName, ConsumerID)

import grpc
import pymongo


class UserAPIServicer(consumer_pb2_grpc.UserAPIServicer):
    """Implements all UserAPI gRPC service methods"""

    async def initialize_db(self):
        """Initialize mongoDB database for consumers"""

        self._consumer_db = ConsumerDB()
        await self._consumer_db.initialize_db()

    async def GetUserByID(self, request: ConsumerID, context: grpc.aio.ServicerContext):
        """Finds consumer by its ID"""

        consumer_in_db = await self._consumer_db.get_user_by_id(request.id)
        return Consumer(username=consumer_in_db.username,
                        full_name=consumer_in_db.full_name,
                        email=consumer_in_db.email,
                        hashed_password=consumer_in_db.hashed_password,
                        created_at=consumer_in_db.created_at,
                        consumer_status=ConsumerStatus(is_active=consumer_in_db.is_active,
                                                       is_verified=consumer_in_db.is_verified))

    async def GetUserByUserName(self, request: ConsumerUserName, context: grpc.aio.ServicerContext):
        """Finds consumer by its username"""
        consumer_in_db = await self._consumer_db.get_user_by_username(request.username)

        # Abort an gRPC error if user is not in db
        if not consumer_in_db:
            context.set_details('User not found')
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return Consumer()

        return Consumer(username=consumer_in_db.username,
                        full_name=consumer_in_db.full_name,
                        email=consumer_in_db.email,
                        hashed_password=consumer_in_db.hashed_password,
                        created_at=consumer_in_db.created_at,
                        consumer_status=ConsumerStatus(is_active=consumer_in_db.is_active,
                                                       is_verified=consumer_in_db.is_verified))

    async def CreateUser(self, request: Consumer, context: grpc.aio.ServicerContext):
        """Create new consumer in database"""

        new_consumer_credentials = {'username': request.username,
                                    'full_name': request.full_name,
                                    'email': request.email,
                                    'hashed_password': request.hashed_password,
                                    'created_at': request.created_at,
                                    'is_active': request.consumer_status.is_active,
                                    'is_verified': request.consumer_status.is_verified}
        try:

            # Create new consumer
            await self._consumer_db.create_user(**new_consumer_credentials)

        except pymongo.errors.DuplicateKeyError as e:

            # Abort an gRPC error if consumer already exists
            context.set_details('User with such credentials already exists')
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            return ConsumerOut()

        consumer_in_db = await self._consumer_db.get_user_by_username(new_consumer_credentials.get('username'))

        response = ConsumerOut(id=str(consumer_in_db.id),
                               username=consumer_in_db.username,
                               email=consumer_in_db.email,
                               consumer_status=ConsumerStatus(is_active=consumer_in_db.is_active,
                                                              is_verified=consumer_in_db.is_verified))

        return response

    async def UpdateUser(self, request: UpdateConsumer, context: grpc.aio.ServicerContext):
        """Update consumer info in database"""

        updated_consumer = await self._consumer_db.update_user(username=request.username,
                                                               full_name=request.new_full_name,
                                                               email=request.new_email)

        return ConsumerOut(id=str(updated_consumer.id),
                           username=updated_consumer.username,
                           email=updated_consumer.email,
                           created_at=updated_consumer.created_at,
                           consumer_status=ConsumerStatus(is_active=updated_consumer.is_active,
                                                          is_verified=updated_consumer.is_verified))

    async def UpdateConsumerStatus(self, request: UpdateStatus, context):
        """Update consumer status"""
        updated_consumer = await self._consumer_db.update_status(username=request.consumer_username.username,
                                                                 is_active=request.consumer_status.is_active,
                                                                 is_verified=request.consumer_status.is_verified)

        return ConsumerOut(id=str(updated_consumer.id),
                           username=updated_consumer.username,
                           email=updated_consumer.email,
                           created_at=updated_consumer.created_at,
                           consumer_status=ConsumerStatus(is_active=updated_consumer.is_active,
                                                          is_verified=updated_consumer.is_verified))

    async def DeleteUser(self, request: Consumer, context: grpc.aio.ServicerContext):
        ...
