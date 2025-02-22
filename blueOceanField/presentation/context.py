from injector import Module, Injector, singleton

from blueOceanField.domain.market import ExchangePlace, IExchange
from blueOceanField.infra.database.database import *
from blueOceanField.infra.database.repository import RepositoryModule
from blueOceanField.infra.exchange import BacktestModule, CryptoExchangeModule
from blueOceanField.presentation.grpc import *


class AppContext:
    injector: Injector
    exchange_contexts: dict[ExchangePlace, Injector] = {}

    def __init__(self):
        AppContext.injector = Injector(
            [
                DatabaseModule("sqlite+aiosqlite:///db.sqlite"),
                RepositoryModule(),
                GrpcModule(),
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
                        if place.name == "backtest"
                        else CryptoExchangeModule(place)
                    )
                ]
            ),
        )
