from injector import Injector

from blueOceanField.application.container.module import *
from blueOceanField.domain.market import ExchangePlace


class AppContext:
    __injector: Injector
    __exchange_contexts: dict[ExchangePlace, "ExchangeContext"] = {}

    @classmethod
    def init(cls) -> None:
        cls.__injector = Injector(
            [
                DatabaseModule(),
                RepositoryModule(),
            ]
        )

    @classmethod
    def get_or_create_exchange_context(cls, place: ExchangePlace) -> "ExchangeContext":
        return cls.__exchange_contexts.setdefault(
            place,
            ExchangeContext(cls.__injector, place),
        )

class ExchangeContext:
    def __init__(self, parent: Injector, place: ExchangePlace):
        self._cache = [] #TODO
        self.injector = Injector(
            modules=[
                ExchangeModule(place),
            ],
            parent=parent,
        )

    def get_or_create_bot_context(self) -> "BotContext":
        return BotContext(self.injector)


class BotContext:
    def __init__(self, parent: Injector):
        self.injector = Injector(parent=parent)
