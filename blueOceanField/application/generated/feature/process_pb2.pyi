from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Constraint(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONSTRAINT_UNSPECIFIED: _ClassVar[Constraint]
    REGEX: _ClassVar[Constraint]
    UPPER_LIMIT: _ClassVar[Constraint]
    LOWER_LIMIT: _ClassVar[Constraint]
    INCLUSION: _ClassVar[Constraint]
    EXCLUSION: _ClassVar[Constraint]
    LENGTH: _ClassVar[Constraint]
    UNIQUE: _ClassVar[Constraint]

class ConstraintTarget(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TARGET_UNSPECIFIED: _ClassVar[ConstraintTarget]
    SELF: _ClassVar[ConstraintTarget]
    KEY: _ClassVar[ConstraintTarget]
    VALUE: _ClassVar[ConstraintTarget]
CONSTRAINT_UNSPECIFIED: Constraint
REGEX: Constraint
UPPER_LIMIT: Constraint
LOWER_LIMIT: Constraint
INCLUSION: Constraint
EXCLUSION: Constraint
LENGTH: Constraint
UNIQUE: Constraint
TARGET_UNSPECIFIED: ConstraintTarget
SELF: ConstraintTarget
KEY: ConstraintTarget
VALUE: ConstraintTarget

class FeatureProcess(_message.Message):
    __slots__ = ("type", "parameters")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    type: str
    parameters: _containers.RepeatedCompositeFieldContainer[FeatureProcessParameter]
    def __init__(self, type: _Optional[str] = ..., parameters: _Optional[_Iterable[_Union[FeatureProcessParameter, _Mapping]]] = ...) -> None: ...

class FeatureProcessParameter(_message.Message):
    __slots__ = ("name", "description", "value", "constraints")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    value: ParameterValue
    constraints: _containers.RepeatedCompositeFieldContainer[ConstraintInfo]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., value: _Optional[_Union[ParameterValue, _Mapping]] = ..., constraints: _Optional[_Iterable[_Union[ConstraintInfo, _Mapping]]] = ...) -> None: ...

class ParameterValue(_message.Message):
    __slots__ = ("int_value", "float_value", "string_value", "bool_value", "list_value", "map_value")
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    LIST_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAP_VALUE_FIELD_NUMBER: _ClassVar[int]
    int_value: int
    float_value: float
    string_value: str
    bool_value: bool
    list_value: ListValue
    map_value: MapValue
    def __init__(self, int_value: _Optional[int] = ..., float_value: _Optional[float] = ..., string_value: _Optional[str] = ..., bool_value: bool = ..., list_value: _Optional[_Union[ListValue, _Mapping]] = ..., map_value: _Optional[_Union[MapValue, _Mapping]] = ...) -> None: ...

class ListValue(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ParameterValue]
    def __init__(self, items: _Optional[_Iterable[_Union[ParameterValue, _Mapping]]] = ...) -> None: ...

class MapValue(_message.Message):
    __slots__ = ("items",)
    class ItemsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ParameterValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ParameterValue, _Mapping]] = ...) -> None: ...
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.MessageMap[str, ParameterValue]
    def __init__(self, items: _Optional[_Mapping[str, ParameterValue]] = ...) -> None: ...

class ConstraintInfo(_message.Message):
    __slots__ = ("type", "target", "args")
    class ArgsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    type: Constraint
    target: ConstraintTarget
    args: _containers.ScalarMap[str, str]
    def __init__(self, type: _Optional[_Union[Constraint, str]] = ..., target: _Optional[_Union[ConstraintTarget, str]] = ..., args: _Optional[_Mapping[str, str]] = ...) -> None: ...
