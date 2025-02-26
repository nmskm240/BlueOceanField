from datetime import datetime

from grpc import ServicerContext
from blueOceanField.application.converter import GrpcConverter
import blueOceanField.application.generated as proto
import blueOceanField.application.usecase as usecase
from blueOceanField.domain.bot import Bot
from blueOceanField.domain.market import IExchange
from blueOceanField.application.container.context import AppContext


class FeatureProcessHandler(proto.FeatureProcessServiceServicer):
    def GetFeatureProcessMeta(self, request, context):
        processes = [GrpcConverter.to_grpc(process) for process in usecase.get_feature_process_metadata()]
        return proto.FeatureProcessMetaResponse(metadata=processes)


class MarketHandler(proto.MarketServiceServicer):
    def GetExchanges(self, request: proto.GetExchangesRequest, context):
        places = [GrpcConverter.to_grpc(place) for place in usecase.get_supported_exchanges()]
        return proto.GetExchangesResponse(exchangePlaces=places)

    async def GetSymbols(self, request: proto.GetSymbolsRequest, context):
        target_exchange = GrpcConverter.from_grpc(request.exchange)
        exchange_context = AppContext.get_or_create_exchange_context(target_exchange)
        symbols = [
            GrpcConverter.to_grpc(symbol)
            for symbol in await usecase.get_supported_symbols_async(exchange_context.injector.get(IExchange))
        ]
        return proto.GetSymbolsResponse(symbols=symbols)

class BotHandler(proto.BotServiceServicer):
    async def CreateBot(self, request: proto.CreateBotRequest, context: ServicerContext):
        symbol = GrpcConverter.from_grpc(request.symbol)

        exchange_context = AppContext.get_or_create_exchange_context(symbol.place)
        bot_context = exchange_context.create_bot_context([GrpcConverter.from_grpc(process) for process in request.processes])
        bot = bot_context.injector.get(Bot)
        bot.run(symbol, from_=datetime(2022, 1, 1), to=datetime(2022, 1, 31))

        yield proto.CreateBotResponse()

