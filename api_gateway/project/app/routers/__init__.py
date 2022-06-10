from project.app.authentication.jwt import Authenticator
from project.grpc.routers.grpc_consumer import GrpcConsumer
from project.app.models.auth_models import Token
from project.app.models.user_models import User, UserOut, UpdateUser

authenticator = Authenticator()
grpc_consumer = GrpcConsumer()
