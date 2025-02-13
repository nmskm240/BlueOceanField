from abc import abstractmethod
from typing import Any, Union


type ParameterType = Union[int, float, str, bool, list, dict, "FeatureProcessParameter"]

class FeatureProcessParameterMeta(type):
    registry: dict[str, dict] = {}

    def __new__(cls, name: str, bases: tuple, namespace: dict[str, Any]):
        new_cls = super().__new__(cls, name, bases, namespace)

        if bases and "FeatureProcessParameter" in bases:
            FeatureProcessParameterMeta.registry[name] = {
                key: value
                for key, value in namespace.items()
                if isinstance(value, FeatureProcessParameter)
            }

        return new_cls

class FeatureProcessParameter[T: ParameterType](metaclass=FeatureProcessParameterMeta):
    def __init__(self, name: str, description: str, value: T):
        self.name = name
        self.description = description
        self.value = value

    def to_dict(self) -> dict:
        """JSON シリアライズ用の辞書形式に変換 (ネスト対応)"""
        if isinstance(self.value, FeatureProcessParameter):
            return {
                "name": self.name,
                "description": self.description,
                "type": "nested",
                "value": self.value.to_dict()
            }
        return {
            "name": self.name,
            "description": self.description,
            "type": type(self.value).__name__,
            "value": self.value
        }

## NOTE: ドメインではなくアプリケーションのほうが合ってる気がする
## MEMO: プラグイン対応するならSDK用のほうには後で変換しやすい形にまでして、本体側でgrpcに詰め替えるような実装になる想定
class FeatureProcessMeta(type):
    """FeatureProcessBase のメタクラス (パラメータのネスト構造を反映)"""
    registry: dict[str, dict] = {}

    def __new__(cls, name: str, bases: tuple, namespace: dict[str, Any]):
        new_cls = super().__new__(cls, name, bases, namespace)

        if bases and FeatureProcessBase in bases:
            parameters = {}

            for key, value in namespace.items():
                if isinstance(value, FeatureProcessParameter):
                    parameters[key] = value.to_dict()

            FeatureProcessMeta.registry[name] = {
                "class_name": name,
                "parameters": parameters
            }

        return new_cls

class FeatureProcessBase(metaclass=FeatureProcessMeta):
    def __init__(self, **kwargs):
        cls_name = self.__class__.__name__
        metadata = FeatureProcessMeta.registry.get(cls_name, {})

        for param_name, param_info in metadata.get("parameters", {}).items():
            default_value = param_info["value"]
            setattr(self, param_name, kwargs.get(param_name, default_value))

    @abstractmethod
    def execute(self, input: dict[str, float]) -> dict[str, float]:
        raise NotImplementedError()

## TODO: 後でプラグインとして切り分ける予定
class Remove(FeatureProcessBase):
    targets = FeatureProcessParameter[list[str]]("targets", "削除対象", [])

    def execute(self, input):
        return {k: v for k, v in input.items() if k not in self.targets}
