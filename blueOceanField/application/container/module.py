from typing import Callable, Type
from injector import Module, provider, singleton
from sqlalchemy import URL, make_url
import blueOceanField.application.generated as proto
from blueOceanField.domain.market import IOhlcvRepository
from blueOceanField.infra.database.database import Database, IDatabase
from blueOceanField.infra.database.repository import OhlcvRepository


class DatabaseModule(Module):
    def __init__(self, url: URL, database: Type[IDatabase] = Database):
        self.url = url
        self._database = database

    @provider
    def url_provider(self) -> URL:
        return make_url(self.url)

    def configure(self, binder):
        binder.bind(IDatabase, to=self._database, scope=singleton)

class RepositoryModule(Module):
    def __init__(self, ohlcv_repository: Type[IOhlcvRepository] = OhlcvRepository):
        self._ohlcv_repository = ohlcv_repository


    def configure(self, binder):
        binder.bind(IOhlcvRepository, to=self._ohlcv_repository, scope=singleton)
