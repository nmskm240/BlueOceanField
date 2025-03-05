import re
from typing import Any

import blueOceanField.application.generated.feature.process_pb2 as feature_proto
import blueOceanField.application.generated.market_pb2 as market_proto
from blueOceanField.domain.feature import *
from blueOceanField.domain.market import ExchangePlace, Symbol


class GrpcConverter:
    _to_grpc_map = {
        ExchangePlace: lambda x: GrpcConverter._exchange_place_to_grpc(x),
        Symbol: lambda x:  GrpcConverter._symbol_to_grpc(x),
        FeatureProcessMetaData: lambda x:  GrpcConverter._feature_process_to_grpc(x),
        FeatureProcessParameter: lambda x: GrpcConverter._feature_process_parameter_to_grpc(x),
    }

    _from_grpc_map = {
        market_proto.ExchangePlace: lambda x: GrpcConverter._grpc_to_exchange_place(x),
        market_proto.Symbol: lambda x: GrpcConverter._grpc_to_symbol(x),
        feature_proto.FeatureProcess: lambda x: GrpcConverter._grpc_to_feature_process(x),
    }

    @staticmethod
    def to_grpc(instance: Any) -> Any:
        if type(instance) in GrpcConverter._to_grpc_map:
            return GrpcConverter._to_grpc_map[type(instance)](instance)
        raise TypeError(f"Unsupported type: {type(instance)}")

    @staticmethod
    def from_grpc(message: Any) -> Any:
        if type(message) in GrpcConverter._from_grpc_map:
            return GrpcConverter._from_grpc_map[type(message)](message)
        raise TypeError(f"Unsupported message type: {type(message)}")

    @staticmethod
    def _symbol_to_grpc(instance: Symbol) -> market_proto.Symbol:
        return market_proto.Symbol(
            code=instance.code,
            name=instance.name,
            exchange=GrpcConverter._exchange_place_to_grpc(instance.place),
        )

    @staticmethod
    def _grpc_to_symbol(message: market_proto.Symbol) -> Symbol:
        return Symbol(
            code=message.code,
            name=message.name,
            place=GrpcConverter._grpc_to_exchange_place(message.exchange),
        )

    @staticmethod
    def _exchange_place_to_grpc(instance: ExchangePlace) -> market_proto.ExchangePlace:
        return market_proto.ExchangePlace(name=instance.name)

    @staticmethod
    def _grpc_to_exchange_place(message: market_proto.ExchangePlace) -> ExchangePlace:
        return ExchangePlace(name=message.name)

    @staticmethod
    def _feature_process_to_grpc(
        instance: FeatureProcessMetaData,
    ) -> feature_proto.FeatureProcess:
        cls_name = instance.type
        metadata = FeatureProcessMeta.registry.get(cls_name)

        if not metadata:
            raise ValueError(f"Unknown FeatureProcess: {cls_name}")

        parameters = [
            GrpcConverter.to_grpc(param) for param in metadata.parameters.values()
        ]

        return feature_proto.FeatureProcess(
            type=metadata.type,
            parameters=parameters,
        )

    @staticmethod
    def _grpc_to_feature_process(
        message: feature_proto.FeatureProcess,
    ) -> FeatureProcessMetaData:
        process_cls = FeatureProcessMeta.registry.get(message.type)

        if not process_cls:
            raise ValueError(f"Unknown FeatureProcess type: {message.type}")

        return process_cls(**message.parameters)

    @staticmethod
    def _feature_process_parameter_to_grpc(
        instance: FeatureProcessParameter,
    ) -> feature_proto.FeatureProcessParameter:
        constraints = [
            GrpcConverter._parameter_constraint_to_grpc(constraint)
            for constraint in instance.constraints
        ]
        return feature_proto.FeatureProcessParameter(
            name=instance.name,
            description=instance.description,
            value=GrpcConverter._parameter_value_to_grpc(instance.value),
            constraints=constraints,
        )

    @staticmethod
    def _grpc_to_feature_process_parameter(
        message: feature_proto.FeatureProcessParameter,
    ) -> FeatureProcessParameter:
        process_cls = FeatureProcessMeta.registry.get(message.type)

        if not process_cls:
            raise ValueError(f"Unknown FeatureProcess type: {message.type}")

        return process_cls(**message.parameters)

    @staticmethod
    def _parameter_value_to_grpc(
        value: ParameterType,
    ) -> feature_proto.ParameterValue:
        match value:
            case bool():
                return feature_proto.ParameterValue(bool_value=value)
            case int():
                return feature_proto.ParameterValue(int_value=value)
            case float():
                return feature_proto.ParameterValue(float_value=value)
            case str():
                return feature_proto.ParameterValue(string_value=value)
            case list():
                elements = [GrpcConverter._parameter_value_to_grpc(e) for e in value]
                return feature_proto.ParameterValue(list_value=feature_proto.ListValue(items=elements))
            case map():
                elements = {
                    key: GrpcConverter._parameter_value_to_grpc(value)
                    for key, value in value.items()
                }
                return feature_proto.ParameterValue(map_value=feature_proto.MapValue(items=elements))
            case _:
                raise ValueError(f"Unknown parameter type: {value}")

    @staticmethod
    def _parameter_constraint_to_grpc(value: Constraint) -> feature_proto.ConstraintInfo:
        target = feature_proto.ConstraintTarget.TARGET_UNSPECIFIED
        match value.target:
            case ConstraintTarget.SELF:
                target = feature_proto.ConstraintTarget.SELF
            case ConstraintTarget.KEY:
                target = feature_proto.ConstraintTarget.KEY
            case ConstraintTarget.VALUE:
                target = feature_proto.ConstraintTarget.VALUE
        words = re.findall(r'[A-Z][a-z]*', value.__class__.__name__)
        return feature_proto.ConstraintInfo(
            type='_'.join(words).upper(),
            target=target,
            args=value.kwargs,
        )
