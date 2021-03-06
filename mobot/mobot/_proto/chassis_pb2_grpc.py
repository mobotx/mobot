# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import chassis_pb2 as chassis__pb2


class ChassisStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ChassisCmdStream = channel.unary_stream(
                '/mobot.Chassis/ChassisCmdStream',
                request_serializer=chassis__pb2.ChassisMetadata.SerializeToString,
                response_deserializer=chassis__pb2.CmdVel.FromString,
                )


class ChassisServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ChassisCmdStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChassisServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ChassisCmdStream': grpc.unary_stream_rpc_method_handler(
                    servicer.ChassisCmdStream,
                    request_deserializer=chassis__pb2.ChassisMetadata.FromString,
                    response_serializer=chassis__pb2.CmdVel.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mobot.Chassis', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Chassis(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ChassisCmdStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mobot.Chassis/ChassisCmdStream',
            chassis__pb2.ChassisMetadata.SerializeToString,
            chassis__pb2.CmdVel.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)