import market_pb2 as _market_pb2
from feature import process_pb2 as _process_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateBotRequest(_message.Message):
    __slots__ = ("name", "symbol", "processes", "start_time", "end_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    PROCESSES_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    symbol: _market_pb2.Symbol
    processes: _containers.RepeatedCompositeFieldContainer[_process_pb2.FeatureProcess]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., symbol: _Optional[_Union[_market_pb2.Symbol, _Mapping]] = ..., processes: _Optional[_Iterable[_Union[_process_pb2.FeatureProcess, _Mapping]]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateBotResponse(_message.Message):
    __slots__ = ("pred_value", "ans_value", "timestamp")
    PRED_VALUE_FIELD_NUMBER: _ClassVar[int]
    ANS_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    pred_value: float
    ans_value: float
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, pred_value: _Optional[float] = ..., ans_value: _Optional[float] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
