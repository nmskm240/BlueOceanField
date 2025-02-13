from feature import process_pb2 as _process_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FeatureProcessMetaRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FeatureProcessMetaResponse(_message.Message):
    __slots__ = ("metadata",)
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _process_pb2.FeatureProcess
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_process_pb2.FeatureProcess, _Mapping]] = ...) -> None: ...
    METADATA_FIELD_NUMBER: _ClassVar[int]
    metadata: _containers.MessageMap[str, _process_pb2.FeatureProcess]
    def __init__(self, metadata: _Optional[_Mapping[str, _process_pb2.FeatureProcess]] = ...) -> None: ...
