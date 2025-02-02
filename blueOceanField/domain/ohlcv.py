from abc import ABCMeta, abstractmethod
from collections.abc import Iterator
from dataclasses import dataclass
from datetime import datetime
from typing import AsyncIterator

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


class IOhlcvRepository(metaclass=ABCMeta):
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
