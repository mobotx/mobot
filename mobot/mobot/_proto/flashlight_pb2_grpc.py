# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import common_pb2 as common__pb2
from . import flashlight_pb2 as flashlight__pb2


class FlashlightStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.FlashlightCmdStream = channel.unary_stream(
                '/mobot.Flashlight/FlashlightCmdStream',
                request_serializer=common__pb2.Empty.SerializeToString,
                response_deserializer=flashlight__pb2.FlashlightState.FromString,
                )


class FlashlightServicer(object):
    """Missing associated documentation comment in .proto file."""

    def FlashlightCmdStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FlashlightServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'FlashlightCmdStream': grpc.unary_stream_rpc_method_handler(
                    servicer.FlashlightCmdStream,
                    request_deserializer=common__pb2.Empty.FromString,
                    response_serializer=flashlight__pb2.FlashlightState.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mobot.Flashlight', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Flashlight(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def FlashlightCmdStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mobot.Flashlight/FlashlightCmdStream',
            common__pb2.Empty.SerializeToString,
            flashlight__pb2.FlashlightState.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)