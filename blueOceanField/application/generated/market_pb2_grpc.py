# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import market_pb2 as market__pb2

GRPC_GENERATED_VERSION = '1.67.1'
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
        + f' but the generated code in market_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class MarketServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetExchanges = channel.unary_unary(
                '/blueOceanField.market.MarketService/GetExchanges',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=market__pb2.ExchangePlaces.FromString,
                _registered_method=True)
        self.GetSymbols = channel.unary_unary(
                '/blueOceanField.market.MarketService/GetSymbols',
                request_serializer=market__pb2.ExchangePlace.SerializeToString,
                response_deserializer=market__pb2.Symbols.FromString,
                _registered_method=True)
        self.Fetch = channel.unary_unary(
                '/blueOceanField.market.MarketService/Fetch',
                request_serializer=market__pb2.Symbol.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


class MarketServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetExchanges(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSymbols(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Fetch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MarketServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetExchanges': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExchanges,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=market__pb2.ExchangePlaces.SerializeToString,
            ),
            'GetSymbols': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSymbols,
                    request_deserializer=market__pb2.ExchangePlace.FromString,
                    response_serializer=market__pb2.Symbols.SerializeToString,
            ),
            'Fetch': grpc.unary_unary_rpc_method_handler(
                    servicer.Fetch,
                    request_deserializer=market__pb2.Symbol.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'blueOceanField.market.MarketService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('blueOceanField.market.MarketService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class MarketService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetExchanges(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/blueOceanField.market.MarketService/GetExchanges',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            market__pb2.ExchangePlaces.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetSymbols(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/blueOceanField.market.MarketService/GetSymbols',
            market__pb2.ExchangePlace.SerializeToString,
            market__pb2.Symbols.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Fetch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/blueOceanField.market.MarketService/Fetch',
            market__pb2.Symbol.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
