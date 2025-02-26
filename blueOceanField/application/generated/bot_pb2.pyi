import market_pb2 as _market_pb2
from feature import process_pb2 as _process_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateBotRequest(_message.Message):
    __slots__ = ("name", "symbol", "processes")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    PROCESSES_FIELD_NUMBER: _ClassVar[int]
    name: str
    symbol: _market_pb2.Symbol
    processes: _containers.RepeatedCompositeFieldContainer[_process_pb2.FeatureProcess]
    def __init__(self, name: _Optional[str] = ..., symbol: _Optional[_Union[_market_pb2.Symbol, _Mapping]] = ..., processes: _Optional[_Iterable[_Union[_process_pb2.FeatureProcess, _Mapping]]] = ...) -> None: ...

class CreateBotResponse(_message.Message):
    __slots__ = ("result",)
    class ResultEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.ScalarMap[str, str]
    def __init__(self, result: _Optional[_Mapping[str, str]] = ...) -> None: ...
