# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: health.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='health.proto',
  package='grpc.health.v1',
  syntax='proto3',
  serialized_pb=_b('\n\x0chealth.proto\x12\x0egrpc.health.v1\"%\n\x12HealthCheckRequest\x12\x0f\n\x07service\x18\x01 \x01(\t\"\x94\x01\n\x13HealthCheckResponse\x12\x41\n\x06status\x18\x01 \x01(\x0e\x32\x31.grpc.health.v1.HealthCheckResponse.ServingStatus\":\n\rServingStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SERVING\x10\x01\x12\x0f\n\x0bNOT_SERVING\x10\x02\x32Z\n\x06Health\x12P\n\x05\x43heck\x12\".grpc.health.v1.HealthCheckRequest\x1a#.grpc.health.v1.HealthCheckResponseb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_HEALTHCHECKRESPONSE_SERVINGSTATUS = _descriptor.EnumDescriptor(
  name='ServingStatus',
  full_name='grpc.health.v1.HealthCheckResponse.ServingStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERVING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_SERVING', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=162,
  serialized_end=220,
)
_sym_db.RegisterEnumDescriptor(_HEALTHCHECKRESPONSE_SERVINGSTATUS)


_HEALTHCHECKREQUEST = _descriptor.Descriptor(
  name='HealthCheckRequest',
  full_name='grpc.health.v1.HealthCheckRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service', full_name='grpc.health.v1.HealthCheckRequest.service', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=69,
)


_HEALTHCHECKRESPONSE = _descriptor.Descriptor(
  name='HealthCheckResponse',
  full_name='grpc.health.v1.HealthCheckResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='grpc.health.v1.HealthCheckResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HEALTHCHECKRESPONSE_SERVINGSTATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=220,
)

_HEALTHCHECKRESPONSE.fields_by_name['status'].enum_type = _HEALTHCHECKRESPONSE_SERVINGSTATUS
_HEALTHCHECKRESPONSE_SERVINGSTATUS.containing_type = _HEALTHCHECKRESPONSE
DESCRIPTOR.message_types_by_name['HealthCheckRequest'] = _HEALTHCHECKREQUEST
DESCRIPTOR.message_types_by_name['HealthCheckResponse'] = _HEALTHCHECKRESPONSE

HealthCheckRequest = _reflection.GeneratedProtocolMessageType('HealthCheckRequest', (_message.Message,), dict(
  DESCRIPTOR = _HEALTHCHECKREQUEST,
  __module__ = 'health_pb2'
  # @@protoc_insertion_point(class_scope:grpc.health.v1.HealthCheckRequest)
  ))
_sym_db.RegisterMessage(HealthCheckRequest)

HealthCheckResponse = _reflection.GeneratedProtocolMessageType('HealthCheckResponse', (_message.Message,), dict(
  DESCRIPTOR = _HEALTHCHECKRESPONSE,
  __module__ = 'health_pb2'
  # @@protoc_insertion_point(class_scope:grpc.health.v1.HealthCheckResponse)
  ))
_sym_db.RegisterMessage(HealthCheckResponse)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class HealthStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.Check = channel.unary_unary(
          '/grpc.health.v1.Health/Check',
          request_serializer=HealthCheckRequest.SerializeToString,
          response_deserializer=HealthCheckResponse.FromString,
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
            request_deserializer=HealthCheckRequest.FromString,
            response_serializer=HealthCheckResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'grpc.health.v1.Health', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaHealthServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def Check(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaHealthStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def Check(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    Check.future = None


  def beta_create_Health_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('grpc.health.v1.Health', 'Check'): HealthCheckRequest.FromString,
    }
    response_serializers = {
      ('grpc.health.v1.Health', 'Check'): HealthCheckResponse.SerializeToString,
    }
    method_implementations = {
      ('grpc.health.v1.Health', 'Check'): face_utilities.unary_unary_inline(servicer.Check),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Health_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('grpc.health.v1.Health', 'Check'): HealthCheckRequest.SerializeToString,
    }
    response_deserializers = {
      ('grpc.health.v1.Health', 'Check'): HealthCheckResponse.FromString,
    }
    cardinalities = {
      'Check': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'grpc.health.v1.Health', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
