from typing import Iterable
import ccxt
from blueOceanField.domain.feature import FeatureProcess, FeatureProcessMeta
from blueOceanField.domain.market import *


def get_feature_process_metadata() -> list[FeatureProcessMeta]:
    return list(FeatureProcessMeta.registry.values())


def get_supported_exchanges() -> list[ExchangePlace]:
    exchanges = [ExchangePlace(e) for e in ccxt.exchanges]
    exchanges.append(ExchangePlace("backtest"))
    return exchanges


async def get_supported_symbols_async(exchange: IExchange) -> list[Symbol]:
    return await exchange.get_all_symbols_async()


def build_feature_pipeline(processes: Iterable[FeatureProcess]) -> rx.Observable:
    return rx.pipe(*[op.map(lambda x: process.execute(x)) for process in processes])
