from datetime import UTC, datetime

from grpc import ServicerContext
from blueOceanField.application.converter import GrpcConverter
import blueOceanField.application.generated as proto
import blueOceanField.application.usecase as usecase
import blueOceanField.application.util as util


class FeatureProcessHandler(proto.FeatureProcessServiceServicer):
    def GetFeatureProcessMeta(self, request: proto.FeatureProcessMetaRequest, context: ServicerContext):
        processes = [GrpcConverter.to_grpc(process) for process in usecase.get_feature_process_metadata()]
        return proto.FeatureProcessMetaResponse(metadata=processes)


class MarketHandler(proto.MarketServiceServicer):
    def GetExchanges(self, request: proto.GetExchangesRequest, context: ServicerContext):
        places = [GrpcConverter.to_grpc(place) for place in usecase.get_supported_exchanges()]
        return proto.GetExchangesResponse(exchangePlaces=places)

    async def GetSymbols(self, request: proto.GetSymbolsRequest, context: ServicerContext):
        target_exchange = GrpcConverter.from_grpc(request.exchange)
        symbols = [
            GrpcConverter.to_grpc(symbol)
            for symbol in await usecase.get_supported_symbols_async(target_exchange)
        ]
        return proto.GetSymbolsResponse(symbols=symbols)

class BotHandler(proto.BotServiceServicer):
    async def CreateBot(self, request: proto.CreateBotRequest, context: ServicerContext):
        processes = [GrpcConverter.from_grpc(process) for process in request.processes]
        symbol = GrpcConverter.from_grpc(request.symbol)
        start_at = request.start_time.ToDatetime(UTC)
        end_at = request.end_time.ToDatetime(UTC)

        async for pred in util.observable_to_async_generator(usecase.bot_run(processes, symbol, start_at, end_at)):
            yield proto.CreateBotResponse(pred_value=pred, ans_value=pred, timestamp=None)
