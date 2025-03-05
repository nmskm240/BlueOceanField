from pathlib import Path
from typing import Type
import ccxt
from injector import Module, inject, provider, singleton
from sqlalchemy import URL
from blueOceanField.domain.bot import Bot
from blueOceanField.domain.market import *
from blueOceanField.infra.config import Config
from blueOceanField.infra.database.database import Database, IDatabase
from blueOceanField.infra.database.repository import OhlcvRepository
from blueOceanField.infra.exchange import BacktestExchange, CryptoExchange


class DatabaseModule(Module):
    @provider
    @singleton
    @inject
    def provide_url(self, config: Config) -> URL:
        return config.database_url

    def configure(self, binder):
        binder.bind(IDatabase, to=Database, scope=singleton)


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
    def configure(self, binder):
        binder.bind(Bot, Bot, scope=singleton)

class ConfigModule(Module):
    def __init__(self, path: Path):
        self.path = path

    @provider
    @singleton
    def provide_config(self) -> Config:
        return Config.from_file(self.path)
