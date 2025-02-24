import pytest
from unittest.mock import AsyncMock
from datetime import UTC, datetime
import ccxt
import rx
from rx.testing import TestScheduler, ReactiveTest
from blueOceanField.domain.market import ExchangePlace, Symbol, Ohlcv
from blueOceanField.infra.exchange import CryptoExchange


@pytest.fixture
def exchange():
    return CryptoExchange(ccxt.binance(), ExchangePlace("Binance"))

@pytest.fixture
def symbol():
    return Symbol(code='BTC/USD', name="BTC/USD", place=ExchangePlace("Binance"))

@pytest.mark.asyncio
async def test_pull_stream(exchange, symbol):
    stream = exchange.pull_stream(
        symbol,
        datetime(2021, 1, 1, 0, 0, 0, tzinfo=UTC),
        datetime(2021, 1, 31, 23, 59, 59, tzinfo=UTC),
    )
    ohlcvs = []

    stream.subscribe(on_next=lambda e: ohlcvs.append(e))

    # Wait for the stream to complete
    await stream

    assert len(ohlcvs) > 0
    for ohlcv in ohlcvs:
        assert isinstance(ohlcv, Ohlcv)
