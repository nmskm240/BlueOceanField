from abc import ABCMeta, abstractmethod
from sqlalchemy import URL
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker


class IDatabase[T: DeclarativeBase](metaclass=ABCMeta):
    @abstractmethod
    def create_async(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def session(self) -> AsyncSession:
        raise NotImplementedError()

    @abstractmethod
    async def close_async(self):
        raise NotImplementedError()

class Database[T: DeclarativeBase](IDatabase[T]):
    def __init__(self, url: URL, base: T):
        self._enigine = create_async_engine(url)
        self._session_factory = async_sessionmaker(
            bind=self._enigine,
            class_=AsyncSession,
            expire_on_commit=False,
            autoflush=False,
        )
        self._base = base
    
    async def create_async(self):
        async with self._enigine.begin() as conn:
            await conn.run_sync(self._base.metadata.create_all)

    def session(self):
        return self._session_factory()
    
    async def close_async(self):
        await self._enigine.dispose()
