from injector import Injector

from blueOceanField.application.container.module import *
from blueOceanField.domain.feature import FeatureProcess
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
        self._bot_contexts: list[BotContext] = []
        self.injector = Injector(
            modules=[
                ExchangeModule(place),
            ],
            parent=parent,
        )

    def get_context(self, id: str) -> "BotContext":
        # TODO
        pass

    def create_bot_context(self, processes: Iterable[FeatureProcess]) -> "BotContext":
        context = BotContext(self.injector)
        self._bot_contexts.append(context)
        return context


class BotContext:
    def __init__(self, parent: Injector, processes: Iterable[FeatureProcess] = []):
        self.injector = Injector(
            modules=[
                BotModule(processes),
            ],
            parent=parent,
        )
