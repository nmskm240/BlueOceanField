import pytest
from datetime import datetime
import sqlalchemy

from blueOceanField.infra.database.repository import OhlcvRepository
from blueOceanField.infra.database.orm.model import Base
from blueOceanField.domain.market import Ohlcv, Symbol, ExchangePlace
from blueOceanField.infra.database.database import Database


DATABASE_URL = "sqlite+aiosqlite:///:memory:"


@pytest.fixture
def pull_target_symbol():
    exchange_place = ExchangePlace(name="NYSE")
    return Symbol(code="AAPL", name="Apple Inc.", place=exchange_place)

@pytest.fixture
def safe_single_symbol_ohlcvs(pull_target_symbol):
    ohlcvs = []
    for i in range(1, 4):
        ohlcvs.append(
            Ohlcv(
                open=100 * i,
                high=105 * i,
                low=95 * i,
                close=102 * i,
                volume=1000 * i,
                symbol=pull_target_symbol,
                decision_at=datetime(2023, 10, i),
            )
        )
    return ohlcvs


@pytest.fixture
def safe_mult_symbol_ohlcvs(pull_target_symbol):
    exchange_place1 = ExchangePlace(name="NYSE")
    exchange_place2 = ExchangePlace(name="NASDAQ")
    symbols = [
        pull_target_symbol,
        Symbol(code="MSFT", name="Microsoft Corp.", place=exchange_place1),
        Symbol(code="MSFT", name="Microsoft Corp.", place=exchange_place2),
    ]

    ohlcv_data = []
    for symbol in symbols:
        for i in range(1, 4):
            ohlcv_data.append(
                Ohlcv(
                    open=100 * i,
                    high=105 * i,
                    low=95 * i,
                    close=102 * i,
                    volume=1000 * i,
                    symbol=symbol,
                    decision_at=datetime(2023, 10, i),
                )
            )
    return ohlcv_data


@pytest.mark.asyncio
async def test_push_and_pull(safe_single_symbol_ohlcvs, pull_target_symbol):
    """OhlcvRepository のデータ保存をテスト"""
    database = Database(sqlalchemy.make_url(DATABASE_URL))
    await database.create_async()
    repository = OhlcvRepository(database)

    # データを挿入
    await repository.push_async(safe_single_symbol_ohlcvs)

    records: list[Ohlcv] = []
    async for e in repository.pull_async(pull_target_symbol):
        records.append(e)

    assert len(records) == len(safe_single_symbol_ohlcvs)


@pytest.mark.asyncio
async def test_push_and_pull_multiple(safe_mult_symbol_ohlcvs, pull_target_symbol):
    """複数の OHLCV データの保存と取得をテスト"""
    database = Database(sqlalchemy.make_url(DATABASE_URL))
    await database.create_async()
    repository = OhlcvRepository(database)
    # データを複数挿入
    await repository.push_async(safe_mult_symbol_ohlcvs)
    records: list[Ohlcv] = []
    async for e in repository.pull_async(pull_target_symbol):
        records.append(e)
    assert len(records) == 3


@pytest.mark.asyncio
async def test_pull_empty(pull_target_symbol):
    """空のデータベースからのデータ取得をテスト"""
    database = Database(sqlalchemy.make_url(DATABASE_URL))
    await database.create_async()
    repository = OhlcvRepository(database)
    records: list[Ohlcv] = []
    async for e in repository.pull_async(pull_target_symbol):
        records.append(e)
    assert len(records) == 0
