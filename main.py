import grpc
from concurrent import futures
from grpc_reflection.v1alpha import reflection

from blueOceanField.application.generated.feature import service_pb2, service_pb2_grpc
from blueOceanField.presentation.grpc import FeatureProcessHandler


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_FeatureProcessServiceServicer_to_server(
        FeatureProcessHandler(), server
    )
    SERVICE_NAMES = (
        service_pb2.DESCRIPTOR.services_by_name['FeatureProcessService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port('[::]:50051')
    server.start()

    server.wait_for_termination()


if __name__ == "__main__":
    main()
