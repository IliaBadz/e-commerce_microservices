from project.grpc.proto.consumer_pb2_grpc import add_UserAPIServicer_to_server
from project.grpc.servicer.api_servicer import UserAPIServicer

user_api_servicer = UserAPIServicer()
