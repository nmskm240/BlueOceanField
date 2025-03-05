from typing import Iterable
import ccxt
from blueOceanField.application.container.context import AppContext
from blueOceanField.domain.bot import Bot
from blueOceanField.domain.feature import FeatureProcess, FeatureProcessMeta
from blueOceanField.domain.market import *


def get_feature_process_metadata() -> list[FeatureProcessMeta]:
    return list(FeatureProcessMeta.registry.values())


def get_supported_exchanges() -> list[ExchangePlace]:
    exchanges = [ExchangePlace(e) for e in ccxt.exchanges]
    exchanges.append(ExchangePlace("backtest"))
    return exchanges


async def get_supported_symbols_async(place: ExchangePlace) -> list[Symbol]:
    exchange_context = AppContext.get_or_create_exchange_context(place)
    exchange = exchange_context.injector.get(IExchange)
    return await exchange.get_all_symbols_async()


def build_feature_pipeline(processes: Iterable[FeatureProcess]) -> rx.Observable:
    return rx.pipe(*[op.map(lambda x: process.execute(x)) for process in processes])


def bot_run(
    processes: Iterable[FeatureProcess],
    symbol: Symbol,
    from_: datetime,
    to: datetime,
) -> rx.Observable:
    exchange_context = AppContext.get_or_create_exchange_context(symbol.place)
    bot_context = exchange_context.create_bot_context(processes)
    bot = bot_context.injector.get(Bot)

    def wrapper():
        bot.run(symbol, from_, to)
        return bot.on_predicated_as_observable

    return rx.defer(lambda _: wrapper())
