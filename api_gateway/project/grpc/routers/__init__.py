from project.grpc.proto.consumer_pb2 import (Consumer, UpdateConsumer, ConsumerUserName,
                                             ConsumerStatus, ConsumerID, UpdateStatus)
from project.grpc.proto.consumer_pb2_grpc import UserAPIStub
from project.grpc.routers.client_config import GrpcClientConfig
from project.settings import settings