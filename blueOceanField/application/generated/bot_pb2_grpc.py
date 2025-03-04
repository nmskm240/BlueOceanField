# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import bot_pb2 as bot__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in bot_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class BotServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateBot = channel.unary_stream(
                '/blueOceanField.bot.BotService/CreateBot',
                request_serializer=bot__pb2.CreateBotRequest.SerializeToString,
                response_deserializer=bot__pb2.CreateBotResponse.FromString,
                _registered_method=True)


class BotServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateBot(self, request, context):
        """TODO: 後でBotの作成と実行を分ける
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BotServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateBot': grpc.unary_stream_rpc_method_handler(
                    servicer.CreateBot,
                    request_deserializer=bot__pb2.CreateBotRequest.FromString,
                    response_serializer=bot__pb2.CreateBotResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'blueOceanField.bot.BotService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('blueOceanField.bot.BotService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class BotService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateBot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/blueOceanField.bot.BotService/CreateBot',
            bot__pb2.CreateBotRequest.SerializeToString,
            bot__pb2.CreateBotResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
