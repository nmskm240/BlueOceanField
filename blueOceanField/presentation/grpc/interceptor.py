import logging
from typing import Callable

import grpc


class LoggingInterceptor(grpc.aio.ServerInterceptor):
    def __init__(self, logger: logging.Logger):
        self.logger = logger

    async def intercept_service(
        self,
        continuation: Callable[[grpc.HandlerCallDetails], grpc.RpcMethodHandler],
        handler_call_details: grpc.HandlerCallDetails,
    ):
        self.logger.info(f"Received gRPC request: {handler_call_details.method}")
        return await continuation(handler_call_details)
