from blueOceanField.application.generated.feature.service_pb2 import FeatureProcessMetaResponse
import blueOceanField.application.generated.feature.service_pb2_grpc as grpc
from blueOceanField.application.usecase import GetFeatureProcessMetadataUsecase


class FeatureProcessHandler(grpc.FeatureProcessServiceServicer):
    def GetFeatureProcessMeta(self, request, context):
        usecase = GetFeatureProcessMetadataUsecase()
        return FeatureProcessMetaResponse(metadata=usecase.execute())
