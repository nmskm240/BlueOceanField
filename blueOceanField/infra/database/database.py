from abc import ABCMeta, abstractmethod

from injector import inject
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from blueOceanField.infra.database.orm.model import Base


class IDatabase(metaclass=ABCMeta):
    @abstractmethod
    def create_async(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def session(self) -> AsyncSession:
        raise NotImplementedError()

    @abstractmethod
    async def close_async(self):
        raise NotImplementedError()


class Database(IDatabase):
    @inject
    def __init__(self, url: URL):
        self._enigine = create_async_engine(url)
        self._session_factory = async_sessionmaker(
            bind=self._enigine,
            class_=AsyncSession,
            expire_on_commit=False,
            autoflush=False,
        )

    async def create_async(self):
        async with self._enigine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    def session(self):
        return self._session_factory()

    async def close_async(self):
        await self._enigine.dispose()
