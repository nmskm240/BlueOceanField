import re
from typing import Any

import blueOceanField.application.generated.feature.process_pb2 as proto
from blueOceanField.domain.feature import *


class GrpcConverter:
    @staticmethod
    def to_grpc(instance: Any) -> Any:
        if isinstance(instance, FeatureProcessMetaData):
            return GrpcConverter._feature_process_to_grpc(instance)
        elif isinstance(instance, FeatureProcessParameter):
            return GrpcConverter._feature_process_parameter_to_grpc(instance)
        raise TypeError(f"Unsupported type: {type(instance)}")

    @staticmethod
    def from_grpc(message: Any) -> Any:
        if isinstance(message, proto.FeatureProcess):
            return GrpcConverter._grpc_to_feature_process(message)
        raise TypeError(f"Unsupported message type: {type(message)}")

    @staticmethod
    def _feature_process_to_grpc(
        instance: FeatureProcessMetaData,
    ) -> proto.FeatureProcess:
        cls_name = instance.type
        metadata = FeatureProcessMeta.registry.get(cls_name)

        if not metadata:
            raise ValueError(f"Unknown FeatureProcess: {cls_name}")

        parameters = [
            GrpcConverter.to_grpc(param) for param in metadata.parameters.values()
        ]

        return proto.FeatureProcess(
            type=metadata.type,
            parameters=parameters,
        )

    @staticmethod
    def _grpc_to_feature_process(
        message: proto.FeatureProcess,
    ) -> FeatureProcessMetaData:
        process_cls = FeatureProcessMeta.registry.get(message.type)

        if not process_cls:
            raise ValueError(f"Unknown FeatureProcess type: {message.type}")

        return process_cls(**message.parameters)

    @staticmethod
    def _feature_process_parameter_to_grpc(
        instance: FeatureProcessParameter,
    ) -> proto.FeatureProcessParameter:
        constraints = [
            GrpcConverter._parameter_constraint_to_grpc(constraint)
            for constraint in instance.constraints
        ]
        return proto.FeatureProcessParameter(
            name=instance.name,
            description=instance.description,
            value=GrpcConverter._parameter_value_to_grpc(instance.value),
            constraints=constraints,
        )

    @staticmethod
    def _grpc_to_feature_process_parameter(
        message: proto.FeatureProcessParameter,
    ) -> FeatureProcessParameter:
        process_cls = FeatureProcessMeta.registry.get(message.type)

        if not process_cls:
            raise ValueError(f"Unknown FeatureProcess type: {message.type}")

        return process_cls(**message.parameters)

    @staticmethod
    def _parameter_value_to_grpc(
        value: ParameterType,
    ) -> proto.ParameterValue:
        match value:
            case bool():
                return proto.ParameterValue(bool_value=value)
            case int():
                return proto.ParameterValue(int_value=value)
            case float():
                return proto.ParameterValue(float_value=value)
            case str():
                return proto.ParameterValue(string_value=value)
            case list():
                elements = [GrpcConverter._parameter_value_to_grpc(e) for e in value]
                return proto.ParameterValue(list_value=proto.ListValue(items=elements))
            case map():
                elements = {
                    key: GrpcConverter._parameter_value_to_grpc(value)
                    for key, value in value.items()
                }
                return proto.ParameterValue(map_value=proto.MapValue(items=elements))
            case _:
                raise ValueError(f"Unknown parameter type: {value}")

    @staticmethod
    def _parameter_constraint_to_grpc(value: Constraint) -> proto.ConstraintInfo:
        target = proto.ConstraintTarget.TARGET_UNSPECIFIED
        match value.target:
            case ConstraintTarget.SELF:
                target = proto.ConstraintTarget.SELF
            case ConstraintTarget.KEY:
                target = proto.ConstraintTarget.KEY
            case ConstraintTarget.VALUE:
                target = proto.ConstraintTarget.VALUE
        words = re.findall(r'[A-Z][a-z]*', value.__class__.__name__)
        return proto.ConstraintInfo(
            type='_'.join(words).upper(),
            target=target,
            args=value.kwargs,
        )
