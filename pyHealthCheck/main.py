"""Reference implementation for health checking in gRPC Python."""

import threading

import grpc

from . import health_pb2
from . import health_pb2_grpc


class HealthServicer(health_pb2_grpc.HealthServicer):
    """Servicer handling RPCs for service statuses."""

    def __init__(self):
        self._server_status_lock = threading.Lock()
        self._server_status = {}

    def Check(self, request, context):
        with self._server_status_lock:
            status = self._server_status.get(request.service)
            if status is None:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                return health_pb2.HealthCheckResponse()
            else:
                return health_pb2.HealthCheckResponse(status=status)

    def SetStatus(self, service, status):
        """Sets the status of a service.
    Args:
        service: string, the name of the service.
            NOTE, '' must be set.
        status: HealthCheckResponse.status enum value indicating
            the status of the service
    """
        with self._server_status_lock:
            self._server_status[service] = status
