from abc import ABCMeta, abstractmethod
from collections.abc import Iterator
from dataclasses import dataclass
from datetime import datetime
from typing import AsyncIterator
import rx

from blueOceanField.domain.exchange import Symbol


@dataclass(frozen=True)
class Ohlcv:
    open: float
    high: float
    low: float
    close: float
    volume: float
    symbol: Symbol
    decision_at: datetime


class IOhlcvSource(metaclass=ABCMeta):
    def pull_stream(
        self,
        symbol: Symbol,
        from_: datetime = datetime.min,
        to: datetime = datetime.max,
    ) -> rx.Observable:
        raise NotImplementedError()


class IOhlcvRepository(IOhlcvSource, metaclass=ABCMeta):
    @abstractmethod
    async def push_async(
        self,
        ohlcvs: Iterator[Ohlcv],
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    async def pull_async(
        self,
        symbol: Symbol,
        from_: datetime = datetime.min,
        to: datetime = datetime.max,
    ) -> AsyncIterator[Ohlcv]:
        raise NotImplementedError
    
    def pull_stream(self, symbol, from_ = datetime.min, to = datetime.max):
        async def handle(observer, scheduler):
            async for e in await self.pull_async(symbol, from_, to):
                observer.on_next(e)
            observer.on_completed()

        return rx.create(handle)
