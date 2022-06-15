import asyncio

from project.grpc.router.grpc_server_config import GrpcServerConfig


grpc_server_config = GrpcServerConfig()
asyncio.run(grpc_server_config.serve())
