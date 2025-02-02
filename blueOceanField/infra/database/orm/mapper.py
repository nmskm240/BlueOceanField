from datetime import UTC, datetime
from blueOceanField.domain.exchange import ExchangePlace, Symbol
from blueOceanField.domain.ohlcv import Ohlcv
from blueOceanField.infra.database.orm.model import ExchangePlaceOrm, OhlcvOrm, SymbolOrm


class ExchangePlaceMapper:
    @staticmethod
    def to_orm(exchange_place: ExchangePlace) -> ExchangePlaceOrm:
        return ExchangePlaceOrm(
            name=exchange_place.name,
        )

    @staticmethod
    def to_domain(orm: ExchangePlaceOrm) -> ExchangePlace:
        return ExchangePlace(
            name=orm.name,
        )

class SymbolMapper:
    @staticmethod
    def to_orm(symbol: Symbol) -> SymbolOrm:
        return SymbolOrm(
            code=symbol.code,
            name=symbol.name,
            place=ExchangePlaceMapper.to_orm(symbol.place),
        )

    @staticmethod
    def to_domain(orm: SymbolOrm) -> Symbol:
        return Symbol(
            code=orm.code,
            name=orm.name,
            place=ExchangePlaceMapper.to_domain(orm.place)
        )

class OhlcvMapper:
    @staticmethod
    def to_orm(ohlcv: Ohlcv) -> OhlcvOrm:
        return OhlcvOrm(
            open=ohlcv.open,
            high=ohlcv.high,
            low=ohlcv.low,
            close=ohlcv.close,
            volume=ohlcv.volume,
            decision_at=ohlcv.decision_at,
            symbol=SymbolMapper.to_orm(ohlcv.symbol),
        )

    @staticmethod
    def to_domain(orm: OhlcvOrm) -> Ohlcv:
        return Ohlcv(
            open=orm.open,
            high=orm.high,
            low=orm.low,
            close=orm.close,
            volume=orm.volume,
            decision_at=orm.decision_at,
            symbol=SymbolMapper.to_domain(orm.symbol),
        )