from typing import Iterable, Optional, Type
import ccxt
from injector import Module, provider, singleton
import rx
from sqlalchemy import URL, make_url
from blueOceanField.application import usecase
from blueOceanField.domain.bot import Bot
from blueOceanField.domain.feature import FeatureProcess
from blueOceanField.domain.market import *
from blueOceanField.infra.database.database import Database, IDatabase
from blueOceanField.infra.database.repository import OhlcvRepository
from blueOceanField.infra.exchange import BacktestExchange, CryptoExchange


class DatabaseModule(Module):
    def __init__(self, database: Type[IDatabase] = Database, url: Optional[URL] = None):
        self.url = (
            url if url is not None else make_url("sqlite+aiosqlite:///:memory:")
        )  # TODO: configから取得する
        self._database = database

    @provider
    @singleton
    def url_provider(self) -> URL:
        return make_url(self.url)

    def configure(self, binder):
        binder.bind(IDatabase, to=self._database, scope=singleton)


class RepositoryModule(Module):
    def __init__(self, ohlcv_repository: Type[IOhlcvRepository] = OhlcvRepository):
        self._ohlcv_repository = ohlcv_repository

    def configure(self, binder):
        binder.bind(IOhlcvRepository, to=self._ohlcv_repository, scope=singleton)


class ExchangeModule(Module):
    def __init__(self, place: ExchangePlace):
        self.place = place

    def configure(self, binder):
        if self.place is BACKTEST_EXCHANGE:
            binder.bind(IExchange, BacktestExchange, scope=singleton)
        else:
            # TODO: 仮想通貨以外もできるように後で書き換える
            binder.bind(IExchange, CryptoExchange, scope=singleton)
            binder.bind(ExchangePlace, self.place)
            binder.bind(ccxt.Exchange, getattr(ccxt, self.place.name), scope=singleton)


class BotModule(Module):
    def __init__(self, processes: Iterable[FeatureProcess]):
        self.processes = processes

    @provider
    @singleton
    def pipeline_provider(self) -> rx.Observable:
        return usecase.build_feature_pipeline(self.processes)

    def configure(self, binder):
        binder.bind(Bot, Bot, scope=singleton)
