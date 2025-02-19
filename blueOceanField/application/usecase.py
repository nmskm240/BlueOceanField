from blueOceanField.application.converter import GrpcConverter
from blueOceanField.application.generated.feature.process_pb2 import FeatureProcess
from blueOceanField.domain.feature import FeatureProcessMeta


class GetFeatureProcessMetadataUsecase:
    def execute(self) -> list[FeatureProcess]:
        messages = []
        for process in FeatureProcessMeta.registry.values():
            messages.append(GrpcConverter.to_grpc(process))
        return messages
