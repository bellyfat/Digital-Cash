# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import digitalCashService_pb2 as digitalCashService__pb2


class digitalCashServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.send = channel.unary_unary(
        '/digitalCashService.digitalCashService/send',
        request_serializer=digitalCashService__pb2.Data.SerializeToString,
        response_deserializer=digitalCashService__pb2.ack.FromString,
        )


class digitalCashServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def send(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_digitalCashServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'send': grpc.unary_unary_rpc_method_handler(
          servicer.send,
          request_deserializer=digitalCashService__pb2.Data.FromString,
          response_serializer=digitalCashService__pb2.ack.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'digitalCashService.digitalCashService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))