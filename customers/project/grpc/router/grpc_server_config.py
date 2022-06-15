import os
from typing import Optional

from project.grpc.proto.consumer_pb2_grpc import add_UserAPIServicer_to_server
from . import user_api_servicer, UserAPIServicer

import grpc


class GrpcServerConfig:
    """Router for starting up a gRPC server"""

    def __init__(self):
        self._aio_server: Optional[grpc.aio.Server, None] = None
        self._consumer_db = None
        self._port: str = os.getenv("GRPC_PORT")
        self._user_api_services: UserAPIServicer = user_api_servicer

    async def serve(self):
        """Initialize database and start gRPC server"""

        # Initialize database for consumer
        await self._user_api_services.initialize_db()

        # Create and run server
        self._aio_server = grpc.aio.server()
        add_UserAPIServicer_to_server(self._user_api_services, self._aio_server)
        self._aio_server.add_insecure_port(self._port)
        await self._aio_server.start()
        await self._aio_server.wait_for_termination()
