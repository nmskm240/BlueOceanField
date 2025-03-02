from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
import re
from typing import Any, Union


type ParameterType = Union[
    int,
    float,
    str,
    bool,
    list[ParameterType],
    dict[str, ParameterType],
]


class ConstraintTarget(Enum):
    UNSPECIFIED = 0
    SELF = 1
    KEY = 2
    VALUE = 3


@dataclass(frozen=True)
class Constraint(ABC):
    target: ConstraintTarget
    kwargs: dict[str, str] = field(default_factory=dict)

    @abstractmethod
    def validate(self, value: ParameterType) -> bool:
        raise NotImplementedError()


class Regex(Constraint):
    def validate(self, value):
        if not isinstance(value, str):
            return False
        return re.match(self.kwargs["pattern"], value) is not None


class UpperLimit(Constraint):
    def validate(self, value):
        return False


class LowerLimit(Constraint):
    def validate(self, value):
        return False


class Inclusion(Constraint):
    def validate(self, value):
        return False


class Exclusion(Constraint):
    def validate(self, value):
        return False


class Length(Constraint):
    def validate(self, value):
        return False


class Unique(Constraint):
    def validate(self, value):
        return False


@dataclass(frozen=True)
class FeatureProcessParameter[T: ParameterType]:
    name: str
    description: str
    value: T
    constraints: list[Constraint] = field(default_factory=list)


@dataclass(frozen=True)
class FeatureProcessMetaData:
    type: str
    parameters: dict[str, FeatureProcessParameter] = field(default_factory=dict)


## NOTE: ドメインではなくアプリケーションのほうが合ってる気がする
class FeatureProcessMeta(type):
    """FeatureProcessBase のメタクラス (パラメータのネスト構造を反映)"""

    registry: dict[str, FeatureProcessMetaData] = {}

    def __new__(cls, name: str, bases: tuple, namespace: dict[str, Any]):
        new_cls = super().__new__(cls, name, bases, namespace)

        if bases and FeatureProcess in bases:
            parameters = {}

            for key, value in namespace.items():
                if isinstance(value, FeatureProcessParameter):
                    parameters[key] = value

            FeatureProcessMeta.registry[name] = FeatureProcessMetaData(name, parameters)

        return new_cls


class FeatureProcess(metaclass=FeatureProcessMeta):
    def __init__(self, **kwargs):
        cls_name = self.__class__.__name__
        metadata = FeatureProcessMeta.registry.get(cls_name, None)

        if not metadata:
            return

        for name, value in metadata.parameters.items():
            setattr(self, name, kwargs.get(name, value.value))

    @abstractmethod
    def execute(self, input: dict[str, float]) -> dict[str, float]:
        # NOTE: dict[str, float] は暫定
        raise NotImplementedError()

## TODO: 後でプラグインとして切り分ける予定
class Remove(FeatureProcess):
    targets = FeatureProcessParameter[list[str]](
        name="targets",
        description="削除対象",
        value=[],
        constraints=[],
    )

    def execute(self, input):
        return {k: v for k, v in input.items() if k not in self.targets}
