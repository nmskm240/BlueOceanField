from abc import ABCMeta, abstractmethod
import asyncio
from collections.abc import Iterator
from dataclasses import dataclass
from datetime import datetime
from typing import AsyncIterator

import rx
import rx.operators as op
import rx.subject


@dataclass(frozen=True)
class Symbol:
    """
    Represents a financial symbol.

    Attributes:
        code (str): The code of the symbol.
        name (str): The name of the symbol.
    """

    code: str
    name: str
    place: "ExchangePlace"

    def __post_init__(self):
        if not self.code:
            raise ValueError("Symbol code cannot be empty")
        if not self.name:
            raise ValueError("Symbol name cannot be empty")


@dataclass(frozen=True)
class ExchangePlace:
    """
    A class representing an exchange place.

    Attributes:
        name (str): The name of the exchange place.

    Raises:
        ValueError: If the name is empty.
    """

    name: str

    def __post_init__(self):
        if not self.name:
            raise ValueError("ExchangePlace name cannot be empty")

BACKTEST_EXCHANGE = ExchangePlace("backtest")

@dataclass(frozen=True)
class Ohlcv:
    """
    A data class representing OHLCV (Open, High, Low, Close, Volume) data for a financial instrument.

    Attributes:
        open (float): The opening price.
        high (float): The highest price.
        low (float): The lowest price.
        close (float): The closing price.
        volume (float): The trading volume.
        symbol (Symbol): The symbol representing the financial instrument.
        decision_at (datetime): The timestamp of the decision.

    Raises:
        ValueError: If any of the price or volume values are less than or equal to 0.
        ValueError: If the low price is greater than the high price.
        ValueError: If the open price is not between the low and high prices.
        ValueError: If the close price is not between the low and high prices.
        ValueError: If the symbol is None.
        ValueError: If the decision time is None.
    """

    open: float
    high: float
    low: float
    close: float
    volume: float
    symbol: Symbol
    decision_at: datetime

    def to_dict(self) -> dict:
        return {
            "open": self.open,
            "high": self.high,
            "low": self.low,
            "close": self.close,
            "volume": self.volume,
            "symbol": self.symbol.code,
            "place": self.symbol.place.name,
            "decision_at": self.decision_at,
        }

    def __post_init__(self):
        if (
            self.open <= 0
            or self.high <= 0
            or self.low <= 0
            or self.close <= 0
            or self.volume <= 0
        ):
            raise ValueError("All price and volume values must be greater than 0")
        if self.low > self.high:
            raise ValueError("Low price cannot be greater than high price")
        if self.open > self.high or self.open < self.low:
            raise ValueError("Open price must be between low and high prices")
        if self.close > self.high or self.close < self.low:
            raise ValueError("Close price must be between low and high prices")
        if self.symbol is None:
            raise ValueError("Symbol cannot be None")
        if self.decision_at is None:
            raise ValueError("Decision time cannot be None")


class IOhlcvSource(metaclass=ABCMeta):
    """
    Interface for OHLCV (Open, High, Low, Close, Volume) data sources.

    Methods
    -------
    pull_stream(symbol: Symbol, from_: datetime = datetime.min, to: datetime = datetime.max) -> rx.Observable
        Abstract method to pull a stream of OHLCV data for a given symbol within a specified date range.
        Parameters:
            symbol (Symbol): The financial instrument symbol for which to pull OHLCV data.
            from_ (datetime, optional): The start date and time for the data stream. Defaults to datetime.min.
            to (datetime, optional): The end date and time for the data stream. Defaults to datetime.max.
        Returns:
            rx.Observable: An observable stream of OHLCV data.
        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
    """

    def pull_stream(
        self,
        symbol: Symbol,
        from_: datetime = datetime.min,
        to: datetime = datetime.max,
    ) -> rx.Observable:
        raise NotImplementedError()


class IOhlcvRepository(IOhlcvSource, metaclass=ABCMeta):
    """
    Interface for OHLCV (Open, High, Low, Close, Volume) repository.
    This interface defines the methods for pushing and pulling OHLCV data asynchronously.
    Methods
    -------
    push_async(ohlcvs: Iterator[Ohlcv]) -> None
        Abstract method to push OHLCV data asynchronously.
    pull_async(symbol: Symbol, from_: datetime = datetime.min, to: datetime = datetime.max) -> AsyncIterator[Ohlcv]
        Abstract method to pull OHLCV data asynchronously for a given symbol and time range.
    pull_stream(symbol, from_ = datetime.min, to = datetime.max)
        Method to pull OHLCV data as an observable stream for a given symbol and time range.
    """

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

    @abstractmethod
    async def get_all_symbols_async(self) -> AsyncIterator[Symbol]:
        raise NotImplementedError

    def pull_stream(
        self,
        symbol: Symbol,
        from_: datetime = datetime.min,
        to: datetime = datetime.max,
    ) -> rx.Observable:
        subject: rx.subject.Subject
        async def handle():
            try:
                async for e in await self.pull_async(symbol, from_, to):
                    subject.on_next(e)
                subject.on_completed()
            except Exception as e:
                subject.on_error(e)

        asyncio.create_task(handle())

        return subject


class IExchange(IOhlcvSource, metaclass=ABCMeta):
    @property
    @abstractmethod
    def place(self) -> ExchangePlace:
        raise NotImplementedError

    async def get_all_symbols_async(self) -> AsyncIterator[Symbol]:
        raise NotImplementedError
