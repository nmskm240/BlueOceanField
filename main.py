import asyncio
import logging
import grpc
from concurrent import futures
from grpc_reflection.v1alpha import reflection

import blueOceanField.application.generated as proto
from blueOceanField.application.container.context import AppContext
from blueOceanField.presentation.grpc.handler import *
from blueOceanField.presentation.grpc.interceptor import *


async def main():
    AppContext.init()

    logger = logging.getLogger("blueOceanField")
    server = grpc.aio.server(
        futures.ThreadPoolExecutor(max_workers=10),
        interceptors=[
            LoggingInterceptor(logger)
        ],
    )
    proto.add_FeatureProcessServiceServicer_to_server(FeatureProcessHandler(), server)
    proto.add_MarketServiceServicer_to_server(MarketHandler(), server)
    proto.add_BotServiceServicer_to_server(BotHandler(), server)
    SERVICE_NAMES = (
        proto.feature_dot_service__pb2.DESCRIPTOR.services_by_name[
            "FeatureProcessService"
        ].full_name,
        proto.market__pb2.DESCRIPTOR.services_by_name["MarketService"].full_name,
        proto.bot__pb2.DESCRIPTOR.services_by_name["BotService"].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port("[::]:50051")
    logger.info("server start")
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.run(main())
