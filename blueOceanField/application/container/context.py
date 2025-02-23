from injector import Module, Injector, singleton

from blueOceanField.application.container.module import *
from blueOceanField.domain.market import ExchangePlace, IExchange
from blueOceanField.infra.exchange import BacktestModule, CryptoExchangeModule


class AppContext:
    injector: Injector
    exchange_contexts: dict[ExchangePlace, Injector] = {}

    def __init__(self):
        AppContext.injector = Injector(
            [
                DatabaseModule("sqlite+aiosqlite:///db.sqlite"),
                RepositoryModule(),
            ]
        )

    @classmethod
    def get_or_create_exchange_context(cls, place: ExchangePlace):
        return cls.exchange_contexts.setdefault(
            place,
            AppContext.injector.create_child_injector(
                [
                    (
                        BacktestModule()
                        if place == ExchangePlace.BACKTEST
                        else CryptoExchangeModule(place)
                    )
                ]
            ),
        )
