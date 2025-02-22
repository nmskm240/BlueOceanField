from injector import Module, inject, singleton
from blueOceanField.application.converter import GrpcConverter
import blueOceanField.application.generated as proto
import blueOceanField.application.usecase as uc
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
        usecase = uc.GetFeatureProcessMetadataUsecase()
        processes = [GrpcConverter.to_grpc(process) for process in usecase.execute()]
        return proto.FeatureProcessMetaResponse(metadata=processes)


class MarketHandler(proto.MarketServiceServicer):
    def GetExchanges(self, request: proto.GetExchangesRequest, context):
        usecase = uc.GetSupportedExchangesUsecase()
        places = [GrpcConverter.to_grpc(place) for place in usecase.execute()]
        return proto.GetExchangesResponse(exchangePlaces=places)

    async def GetSymbols(self, request: proto.GetSymbolsRequest, context):
        from blueOceanField.presentation.context import AppContext

        target_exchange = GrpcConverter.from_grpc(request.exchange)
        exchange_context = AppContext.get_or_create_exchange_context(target_exchange)
        usecase = uc.GetSupportedSymbolsUsecase()
        symbols = [
            GrpcConverter.to_grpc(symbol)
            for symbol in await usecase.execute_async(exchange_context.get(IExchange))
        ]
        return proto.GetSymbolsResponse(symbols=symbols)
