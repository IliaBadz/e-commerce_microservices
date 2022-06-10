from . import UserAPIStub

import grpc


class GrpcClientConfig:
    def __init__(self):
        self.channel = None
        self.stub = None
        self.response = None

    def create_channel(self, target, options=None, compression=None, interceptors=None):
        self.channel = grpc.aio.insecure_channel(target, options, compression, interceptors)
        return self.channel

    def get_stub(self):
        self.stub = UserAPIStub(self.channel)
        return self.stub

    async def close_channel(self):
        await self.channel.close()
