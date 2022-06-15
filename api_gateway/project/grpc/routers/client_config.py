from . import UserAPIStub

import grpc


class GrpcClientConfig:
    """Provides methods for creating gRPC client"""

    def __init__(self):
        self.channel = None
        self.stub = None
        self.response = None

    def create_channel(self, target, options=None, compression=None, interceptors=None):
        """Creates asynchronous channel"""
        self.channel = grpc.aio.insecure_channel(target, options, compression, interceptors)
        return self.channel

    def get_stub(self):
        """
        Returns stub

        Stub wraps a Channel and uses it to send RPCs to the service.

        :return: Stub that is used for calling methods defined by the ``UserAPI`` service
        :rtype: `UserAPIStub`

        """
        self.stub = UserAPIStub(self.channel)
        return self.stub

    async def close_channel(self):
        """Closes channel"""

        await self.channel.close()
