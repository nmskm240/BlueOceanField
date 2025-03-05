import asyncio
from datetime import datetime, UTC
from typing import AsyncGenerator, Optional

import ccxt
import rx
from rx.core.observable.connectableobservable import ConnectableObservable
import rx.operators as op
from injector import Module, inject, provider
import rx.subject

from blueOceanField.domain.market import *


class CryptoExchange(IExchange):
    FETCH_LIMIT = 1000
    SEC_PER_MILSEC = 1000

    @inject
    def __init__(self, client: ccxt.Exchange, place: ExchangePlace):
        self.__client = client
        self.__place = place

    @property
    def place(self) -> ExchangePlace:
        return self.__place

    def pull_stream(
        self,
        symbol: Symbol,
        from_: datetime = datetime.min,
        to: datetime = datetime.max,
    ) -> rx.Observable:
        return rx.create(lambda observer, _: self.__create_ohlcv_stream(observer, symbol, from_, to))

    def __create_ohlcv_stream(
        self,
        observer: rx.core.Observer,
        symbol: Symbol,
        from_: datetime,
        to: datetime,
    ) -> None:
        async def handle():
            try:
                async for e in self.__fetch_ohlcv(symbol, from_, to):
                    observer.on_next(e)
                observer.on_completed()
            except Exception as e:
                observer.on_error(e)

        asyncio.create_task(handle())

    async def get_all_symbols_async(self):
        if not self.__client.has["fetchMarkets"]:
            return []
        markets = self.__client.fetch_markets()
        if not markets:
            return []
        return [
            Symbol(market["id"], market["symbol"], self.place) for market in markets
        ]

    async def __fetch_ohlcv(
        self, symbol: Symbol, from_: datetime, to: datetime
    ) -> AsyncGenerator[Ohlcv, None]:
        if not self.__client.has["fetchOHLCV"]:
            return
        while from_ < to:
            fetched = self.__client.fetch_ohlcv(
                symbol.code,
                since=int(from_.timestamp()) * CryptoExchange.SEC_PER_MILSEC,
                limit=CryptoExchange.FETCH_LIMIT,
            )
            if not fetched:
                break
            for ohlcv in fetched:
                yield Ohlcv(
                    open=ohlcv[1],
                    high=ohlcv[2],
                    low=ohlcv[3],
                    close=ohlcv[4],
                    volume=ohlcv[5],
                    symbol=symbol,
                    decision_at=datetime.fromtimestamp(
                        ohlcv[0] / CryptoExchange.SEC_PER_MILSEC
                    ),
                )
            from_ = datetime.fromtimestamp(
                fetched[-1][0] / CryptoExchange.SEC_PER_MILSEC, tz=UTC
            )


class BacktestExchange(IExchange):
    @inject
    def __init__(self, source: IOhlcvRepository):
        self.__source = source

    @property
    def place(self) -> ExchangePlace:
        return BACKTEST_EXCHANGE

    def pull_stream(
        self,
        symbol: Symbol,
        from_: datetime = datetime.min,
        to: datetime = datetime.max,
    ) -> rx.Observable:
        return rx.defer(lambda: self.__source.pull_stream(symbol, from_, to))

    async def get_all_symbols_async(self):
        return await self.__source.get_all_symbols_async()
