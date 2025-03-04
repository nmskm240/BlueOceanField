from abc import abstractmethod
import sqlalchemy as sql
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()

class ExchangePlaceOrm(Base):
    __tablename__ = "exchange_places"

    id = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.String, nullable=False, unique=True)

    def to_dict(self) -> dict:
        return {"name": self.name}


class SymbolOrm(Base):
    __tablename__ = "symbols"

    id = sql.Column(sql.Integer, primary_key=True)
    code = sql.Column(sql.String)
    name = sql.Column(sql.String)
    place_id = sql.Column(sql.Integer, sql.ForeignKey("exchange_places.id"), nullable=False)

    place = relationship("ExchangePlaceOrm", foreign_keys=[place_id], backref="exchange_places")

    __table_args__ = (
        sql.UniqueConstraint("code", "place_id", name="unique_idx_code_place_id"),
    )

    def to_dict(self) -> dict:
        return {
            "code": self.code,
            "name": self.name,
            "place_id": self.place_id,
        }


class OhlcvOrm(Base):
    __tablename__ = "ohlcvs"

    open = sql.Column(sql.Float)
    high = sql.Column(sql.Float)
    low = sql.Column(sql.Float)
    close = sql.Column(sql.Float)
    volume = sql.Column(sql.Float)
    symbol_id = sql.Column(sql.Integer, sql.ForeignKey("symbols.id"), primary_key=True, nullable=False)
    decision_at = sql.Column(sql.DateTime(timezone=True), index=True, primary_key=True, nullable=False)

    symbol = relationship("SymbolOrm", foreign_keys=[symbol_id], backref="symbols")

    __table_args__ = (
        sql.UniqueConstraint(
            "symbol_id", "decision_at", name="unique_idx_symbol_id_decision_at"
        ),
    )

    def to_dict(self) -> dict:
        return {
            "open": self.open,
            "high": self.high,
            "low": self.low,
            "close": self.close,
            "volume": self.volume,
            "symbol_id": self.symbol_id,
            "decision_at": self.decision_at,
        }
