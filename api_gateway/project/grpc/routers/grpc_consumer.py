import datetime

from . import (Consumer, UpdateConsumer,
               ConsumerUserName, ConsumerStatus,
               ConsumerID, UpdateStatus,
               UserAPIStub, GrpcClientConfig, settings)


import grpc
from google.protobuf.json_format import MessageToDict


class GrpcConsumer:
    """Implements `UserAPI` service methods for making RPC requests"""

    def __init__(self):
        self.grpc_client: GrpcClientConfig = GrpcClientConfig()
        self._channel: grpc.aio.Channel = self.grpc_client.create_channel(settings.GRPC_SERVER_ADDRESS)
        self._stub: UserAPIStub = self.grpc_client.get_stub()

    async def get_user_by_id(self, user_id: str) -> dict:
        consumer = await self._stub.GetUserByID(ConsumerID(id=user_id))
        return MessageToDict(message=consumer, preserving_proto_field_name=True)

    async def get_user_by_username(self, username: str):
        consumer = await self._stub.GetUserByUserName(ConsumerUserName(username=username))
        return MessageToDict(message=consumer, preserving_proto_field_name=True)

    async def create_user(self, username: str,
                          full_name: str,
                          email: str,
                          hashed_password: str,
                          created_at: datetime.datetime,
                          is_active: bool = False,
                          is_verified: bool = False) -> dict:
        grpc_request = Consumer(username=username,
                                full_name=full_name,
                                email=email,
                                hashed_password=hashed_password,
                                created_at=created_at.strftime("%m/%d/%Y, %H:%M:%S"),
                                consumer_status=ConsumerStatus(is_active=is_active,
                                                               is_verified=is_verified))
        consumer = await self._stub.CreateUser(grpc_request)
        return MessageToDict(message=consumer, preserving_proto_field_name=True)

    async def update_user(self, username: str, full_name: str, email: str) -> dict:
        grpc_request = UpdateConsumer(username=username,
                                      new_full_name=full_name,
                                      new_email=email)

        updated_consumer = await self._stub.UpdateUser(grpc_request)

        return MessageToDict(message=updated_consumer, preserving_proto_field_name=True)

    async def update_status(self, username: str, is_active: bool = False, is_verified: bool = False) -> dict:

        grpc_request = UpdateStatus(consumer_username=ConsumerUserName(username=username),
                                    consumer_status=ConsumerStatus(is_active=is_active, is_verified=is_verified))

        updated_status_consumer = await self._stub.UpdateConsumerStatus(grpc_request)

        return MessageToDict(updated_status_consumer)

    async def delete_user(self, username: str):
        grpc_request = UpdateStatus(consumer_username=ConsumerUserName(username=username),
                                    consumer_status=ConsumerStatus(is_active=False, is_verified=False))

        await self._stub.UpdateConsumerStatus(grpc_request)
