# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import health_pb2 as health__pb2


class HealthStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Check = channel.unary_unary(
        '/grpc.health.v1.Health/Check',
        request_serializer=health__pb2.HealthCheckRequest.SerializeToString,
        response_deserializer=health__pb2.HealthCheckResponse.FromString,
        )


class HealthServicer(object):

  def Check(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_HealthServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Check': grpc.unary_unary_rpc_method_handler(
          servicer.Check,
          request_deserializer=health__pb2.HealthCheckRequest.FromString,
          response_serializer=health__pb2.HealthCheckResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpc.health.v1.Health', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
