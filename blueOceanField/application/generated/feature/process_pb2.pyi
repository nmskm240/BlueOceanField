from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FeatureProcess(_message.Message):
    __slots__ = ("class_name", "parameters")
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: FeatureProcessParameter
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[FeatureProcessParameter, _Mapping]] = ...) -> None: ...
    CLASS_NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    class_name: str
    parameters: _containers.MessageMap[str, FeatureProcessParameter]
    def __init__(self, class_name: _Optional[str] = ..., parameters: _Optional[_Mapping[str, FeatureProcessParameter]] = ...) -> None: ...

class FeatureProcessParameter(_message.Message):
    __slots__ = ("name", "description", "type", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    type: str
    value: ParameterValue
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[str] = ..., value: _Optional[_Union[ParameterValue, _Mapping]] = ...) -> None: ...

class ParameterValue(_message.Message):
    __slots__ = ("nested", "int_value", "float_value", "string_value", "bool_value", "string_list_value", "string_float_map_value")
    NESTED_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_LIST_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_FLOAT_MAP_VALUE_FIELD_NUMBER: _ClassVar[int]
    nested: FeatureProcessParameter
    int_value: int
    float_value: float
    string_value: str
    bool_value: bool
    string_list_value: StringListValue
    string_float_map_value: StringFloatMapValue
    def __init__(self, nested: _Optional[_Union[FeatureProcessParameter, _Mapping]] = ..., int_value: _Optional[int] = ..., float_value: _Optional[float] = ..., string_value: _Optional[str] = ..., bool_value: bool = ..., string_list_value: _Optional[_Union[StringListValue, _Mapping]] = ..., string_float_map_value: _Optional[_Union[StringFloatMapValue, _Mapping]] = ...) -> None: ...

class StringListValue(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, items: _Optional[_Iterable[str]] = ...) -> None: ...

class StringFloatMapValue(_message.Message):
    __slots__ = ("items",)
    class ItemsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.ScalarMap[str, float]
    def __init__(self, items: _Optional[_Mapping[str, float]] = ...) -> None: ...
