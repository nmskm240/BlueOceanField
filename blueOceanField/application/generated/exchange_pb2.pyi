from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangePlace(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ExchangePlaces(_message.Message):
    __slots__ = ("exchangePlaces",)
    EXCHANGEPLACES_FIELD_NUMBER: _ClassVar[int]
    exchangePlaces: _containers.RepeatedCompositeFieldContainer[ExchangePlace]
    def __init__(self, exchangePlaces: _Optional[_Iterable[_Union[ExchangePlace, _Mapping]]] = ...) -> None: ...

class Symbol(_message.Message):
    __slots__ = ("code", "name", "exchange")
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    code: str
    name: str
    exchange: ExchangePlace
    def __init__(self, code: _Optional[str] = ..., name: _Optional[str] = ..., exchange: _Optional[_Union[ExchangePlace, _Mapping]] = ...) -> None: ...

class Symbols(_message.Message):
    __slots__ = ("symbols",)
    SYMBOLS_FIELD_NUMBER: _ClassVar[int]
    symbols: _containers.RepeatedCompositeFieldContainer[Symbol]
    def __init__(self, symbols: _Optional[_Iterable[_Union[Symbol, _Mapping]]] = ...) -> None: ...
