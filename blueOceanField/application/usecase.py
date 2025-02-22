import ccxt
from blueOceanField.domain.feature import FeatureProcessMeta
from blueOceanField.domain.market import ExchangePlace, IExchange, IOhlcvRepository, Symbol


class GetFeatureProcessMetadataUsecase:
    def execute(self) -> list[FeatureProcessMeta]:
        return list(FeatureProcessMeta.registry.values())


class GetSupportedExchangesUsecase:
    def execute(self) -> list[ExchangePlace]:
        exchanges = [ExchangePlace(e) for e in ccxt.exchanges]
        exchanges.append(ExchangePlace("backtest"))
        return exchanges


class GetSupportedSymbolsUsecase:
    async def execute_async(self, exchange: IExchange) -> list[Symbol]:
        return await exchange.get_all_symbols_async()
