import asyncio
from datetime import datetime, UTC
from typing import AsyncGenerator

import ccxt
import rx
from rx.core.observable.connectableobservable import ConnectableObservable
import rx.operators as op
from injector import inject
import rx.subject

from blueOceanField.domain.market import IExchange, Symbol, IOhlcvSource, Ohlcv


class CryptoExchange(IExchange):
    FETCH_LIMIT = 1000
    SEC_PER_MILSEC = 1000

    @inject
    def __init__(self, client: ccxt.Exchange):
        self.__client = client

    def pull_stream(
        self,
        symbol: Symbol,
        from_: datetime = datetime.min,
        to: datetime = datetime.max,
    ) -> ConnectableObservable:
        subject = rx.subject.Subject()
        async def handle():
            try:
                async for e in self.__fetch_ohlcv(symbol, from_, to):
                    subject.on_next(e)
                subject.on_completed()
            except Exception as e:
                subject.on_error(e)

        asyncio.create_task(handle())

        return subject

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
                    decision_at=datetime.fromtimestamp(ohlcv[0] / CryptoExchange.SEC_PER_MILSEC),
                )
            from_ = datetime.fromtimestamp(fetched[-1][0] / CryptoExchange.SEC_PER_MILSEC, tz=UTC)


class BacktestExchange(IExchange):
    @inject
    def __init__(self, source: IOhlcvSource):
        self.__source = source

    def pull_stream(
        self,
        symbol: Symbol,
        from_: datetime = datetime.min,
        to: datetime = datetime.max,
    ) -> rx.Observable:
        return self.__source.pull_stream(symbol, from_, to)
