from abc import ABCMeta
from dataclasses import dataclass


@dataclass(frozen=True)
class ExchangePlace:
    name: str


@dataclass(frozen=True)
class Symbol:
    code: str
    name: str
    place: ExchangePlace


class IExchange(metaclass=ABCMeta):
    pass
