import asyncio

from project.grpc.router.grpc_server_router import GrpcServerRouter


grpc_server_router = GrpcServerRouter()
asyncio.run(grpc_server_router.serve())
