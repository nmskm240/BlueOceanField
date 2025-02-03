from datetime import datetime
from typing import Iterator, Type

from sqlalchemy import insert, select
from sqlalchemy.dialects.sqlite import insert as sqlite_insert
from sqlalchemy.orm import joinedload
import sqlalchemy.ext
import sqlalchemy.ext.asyncio
from blueOceanField.domain.exchange import ExchangePlace
from blueOceanField.domain.ohlcv import IOhlcvRepository, Ohlcv
from blueOceanField.infra.database.database import IDatabase
from blueOceanField.infra.database.orm.mapper import (
    ExchangePlaceMapper,
    OhlcvMapper,
    SymbolMapper,
)
from blueOceanField.infra.database.orm.model import (
    ExchangePlaceOrm,
    OhlcvBase,
    OhlcvOrm,
    SymbolOrm,
)


class OhlcvRepository(IOhlcvRepository):
    def __init__(self, database: IDatabase):
        self.__database = database

    async def push_async(self, ohlcvs):
        """OHLCVデータを非同期でデータベースに保存"""
        async with self.__database.session() as session:
            async with session.begin() as transaction:
                place_and_symbols: set[tuple[ExchangePlace, SymbolOrm]] = {
                    (ohlcv.symbol.place, SymbolMapper.to_orm(ohlcv.symbol))
                    for ohlcv in ohlcvs
                }
                exchange_places: set[ExchangePlaceOrm] = {
                    ExchangePlaceMapper.to_orm(place) for place, _ in place_and_symbols
                }

                saved_places: dict[str, ExchangePlaceOrm] = {
                    place.name: place
                    for place in await self.__upsert_async(
                        ExchangePlaceOrm, exchange_places, session, ["name"]
                    )
                }

                symbols: list[SymbolOrm] = []
                for place, symbol in place_and_symbols:
                    if symbol.place_id is None:
                        symbol.place_id = saved_places[place.name].id
                    symbols.append(symbol)
                saved_symbols: dict[tuple[str, int], SymbolOrm] = {
                    (symbol.code, symbol.place_id): symbol
                    for symbol in await self.__upsert_async(
                        SymbolOrm, symbols, session, ["code", "place_id"]
                    )
                }

                ohlcv_orms = []
                for ohlcv in ohlcvs:
                    orm = OhlcvMapper.to_orm(ohlcv)
                    if orm.symbol_id is None:
                        key = (
                            ohlcv.symbol.code,
                            saved_places[ohlcv.symbol.place.name].id,
                        )
                        orm.symbol_id = saved_symbols[key].id
                    ohlcv_orms.append(orm.to_dict())

                if ohlcv_orms:
                    stmt = (
                        sqlite_insert(OhlcvOrm)
                        .values(ohlcv_orms)
                        .on_conflict_do_nothing(
                            index_elements=["symbol_id", "decision_at"]
                        )
                    )
                    await session.execute(stmt)

    async def pull_async(self, symbol, from_=datetime.min, to=datetime.max):
        """指定したシンボルと期間のOHLCVデータを取得"""
        async with self.__database.session() as session:
            result = await session.execute(
                select(OhlcvOrm)
                .options(joinedload(OhlcvOrm.symbol).joinedload(SymbolOrm.place))
                .join(SymbolOrm)
                .join(ExchangePlaceOrm)
                .where(
                    SymbolOrm.code == symbol.code,
                    ExchangePlaceOrm.name == symbol.place.name,
                    OhlcvOrm.decision_at >= from_,
                    OhlcvOrm.decision_at < to,
                )
            )
            ohlcvs = result.scalars()
            for ohlcv in ohlcvs:
                yield Ohlcv(
                    open=ohlcv.open,
                    high=ohlcv.high,
                    low=ohlcv.low,
                    close=ohlcv.close,
                    volume=ohlcv.volume,
                    symbol=symbol,
                    decision_at=ohlcv.decision_at,
                )

    async def __upsert_async[
        T: OhlcvBase
    ](
        self,
        orm: Type,
        elements: Iterator[T],
        session: sqlalchemy.ext.asyncio.AsyncSession,
        conflict_columns: list[str],
    ) -> Iterator[T]:
        """要素を挿入または更新"""
        res: list[T] = []
        for element in elements:
            stmt = (
                sqlite_insert(orm)
                .values(element.to_dict())
                .on_conflict_do_update(
                    index_elements=conflict_columns, set_=element.to_dict()
                )
                .returning(orm)
            )
            result = await session.execute(stmt)
            res.extend(result.scalars().all())
        return res
