from injector import Module, inject, singleton
from blueOceanField.application.converter import GrpcConverter
import blueOceanField.application.generated as proto
import blueOceanField.application.usecase as usecase
from blueOceanField.domain.market import IExchange, IOhlcvRepository


class GrpcModule(Module):
    def configure(self, binder):
        binder.bind(
            proto.FeatureProcessServiceServicer,
            to=FeatureProcessHandler,
            scope=singleton,
        )
        binder.bind(proto.MarketServiceServicer, to=MarketHandler, scope=singleton)


class FeatureProcessHandler(proto.FeatureProcessServiceServicer):
    def GetFeatureProcessMeta(self, request, context):
        processes = [GrpcConverter.to_grpc(process) for process in usecase.get_feature_process_metadata()]
        return proto.FeatureProcessMetaResponse(metadata=processes)


class MarketHandler(proto.MarketServiceServicer):
    def GetExchanges(self, request: proto.GetExchangesRequest, context):
        places = [GrpcConverter.to_grpc(place) for place in usecase.get_supported_exchanges()]
        return proto.GetExchangesResponse(exchangePlaces=places)

    async def GetSymbols(self, request: proto.GetSymbolsRequest, context):
        from blueOceanField.presentation.context import AppContext

        target_exchange = GrpcConverter.from_grpc(request.exchange)
        exchange_context = AppContext.get_or_create_exchange_context(target_exchange)
        symbols = [
            GrpcConverter.to_grpc(symbol)
            for symbol in await usecase.get_supported_symbols_async(exchange_context.get(IExchange))
        ]
        return proto.GetSymbolsResponse(symbols=symbols)
