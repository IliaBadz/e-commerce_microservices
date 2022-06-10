# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from project.grpc.proto import consumer_pb2 as project_dot_grpc_dot_proto_dot_consumer__pb2


class UserAPIStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUserByID = channel.unary_unary(
                '/consumer.UserAPI/GetUserByID',
                request_serializer=project_dot_grpc_dot_proto_dot_consumer__pb2.ConsumerID.SerializeToString,
                response_deserializer=project_dot_grpc_dot_proto_dot_consumer__pb2.Consumer.FromString,
                )
        self.GetUserByUserName = channel.unary_unary(
                '/consumer.UserAPI/GetUserByUserName',
                request_serializer=project_dot_grpc_dot_proto_dot_consumer__pb2.ConsumerUserName.SerializeToString,
                response_deserializer=project_dot_grpc_dot_proto_dot_consumer__pb2.Consumer.FromString,
                )
        self.CreateUser = channel.unary_unary(
                '/consumer.UserAPI/CreateUser',
                request_serializer=project_dot_grpc_dot_proto_dot_consumer__pb2.Consumer.SerializeToString,
                response_deserializer=project_dot_grpc_dot_proto_dot_consumer__pb2.ConsumerOut.FromString,
                )
        self.UpdateUser = channel.unary_unary(
                '/consumer.UserAPI/UpdateUser',
                request_serializer=project_dot_grpc_dot_proto_dot_consumer__pb2.UpdateConsumer.SerializeToString,
                response_deserializer=project_dot_grpc_dot_proto_dot_consumer__pb2.ConsumerOut.FromString,
                )
        self.UpdateConsumerStatus = channel.unary_unary(
                '/consumer.UserAPI/UpdateConsumerStatus',
                request_serializer=project_dot_grpc_dot_proto_dot_consumer__pb2.UpdateStatus.SerializeToString,
                response_deserializer=project_dot_grpc_dot_proto_dot_consumer__pb2.ConsumerOut.FromString,
                )
        self.DeleteUser = channel.unary_unary(
                '/consumer.UserAPI/DeleteUser',
                request_serializer=project_dot_grpc_dot_proto_dot_consumer__pb2.ConsumerUserName.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class UserAPIServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetUserByID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserByUserName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateConsumerStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetUserByID': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserByID,
                    request_deserializer=project_dot_grpc_dot_proto_dot_consumer__pb2.ConsumerID.FromString,
                    response_serializer=project_dot_grpc_dot_proto_dot_consumer__pb2.Consumer.SerializeToString,
            ),
            'GetUserByUserName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserByUserName,
                    request_deserializer=project_dot_grpc_dot_proto_dot_consumer__pb2.ConsumerUserName.FromString,
                    response_serializer=project_dot_grpc_dot_proto_dot_consumer__pb2.Consumer.SerializeToString,
            ),
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=project_dot_grpc_dot_proto_dot_consumer__pb2.Consumer.FromString,
                    response_serializer=project_dot_grpc_dot_proto_dot_consumer__pb2.ConsumerOut.SerializeToString,
            ),
            'UpdateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUser,
                    request_deserializer=project_dot_grpc_dot_proto_dot_consumer__pb2.UpdateConsumer.FromString,
                    response_serializer=project_dot_grpc_dot_proto_dot_consumer__pb2.ConsumerOut.SerializeToString,
            ),
            'UpdateConsumerStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateConsumerStatus,
                    request_deserializer=project_dot_grpc_dot_proto_dot_consumer__pb2.UpdateStatus.FromString,
                    response_serializer=project_dot_grpc_dot_proto_dot_consumer__pb2.ConsumerOut.SerializeToString,
            ),
            'DeleteUser': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteUser,
                    request_deserializer=project_dot_grpc_dot_proto_dot_consumer__pb2.ConsumerUserName.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'consumer.UserAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserAPI(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetUserByID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/consumer.UserAPI/GetUserByID',
            project_dot_grpc_dot_proto_dot_consumer__pb2.ConsumerID.SerializeToString,
            project_dot_grpc_dot_proto_dot_consumer__pb2.Consumer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserByUserName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/consumer.UserAPI/GetUserByUserName',
            project_dot_grpc_dot_proto_dot_consumer__pb2.ConsumerUserName.SerializeToString,
            project_dot_grpc_dot_proto_dot_consumer__pb2.Consumer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/consumer.UserAPI/CreateUser',
            project_dot_grpc_dot_proto_dot_consumer__pb2.Consumer.SerializeToString,
            project_dot_grpc_dot_proto_dot_consumer__pb2.ConsumerOut.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/consumer.UserAPI/UpdateUser',
            project_dot_grpc_dot_proto_dot_consumer__pb2.UpdateConsumer.SerializeToString,
            project_dot_grpc_dot_proto_dot_consumer__pb2.ConsumerOut.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateConsumerStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/consumer.UserAPI/UpdateConsumerStatus',
            project_dot_grpc_dot_proto_dot_consumer__pb2.UpdateStatus.SerializeToString,
            project_dot_grpc_dot_proto_dot_consumer__pb2.ConsumerOut.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/consumer.UserAPI/DeleteUser',
            project_dot_grpc_dot_proto_dot_consumer__pb2.ConsumerUserName.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)