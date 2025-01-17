# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import collections_pb2 as collections__pb2


class CollectionsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/qdrant.Collections/Get',
                request_serializer=collections__pb2.GetCollectionInfoRequest.SerializeToString,
                response_deserializer=collections__pb2.GetCollectionInfoResponse.FromString,
                )
        self.List = channel.unary_unary(
                '/qdrant.Collections/List',
                request_serializer=collections__pb2.ListCollectionsRequest.SerializeToString,
                response_deserializer=collections__pb2.ListCollectionsResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/qdrant.Collections/Create',
                request_serializer=collections__pb2.CreateCollection.SerializeToString,
                response_deserializer=collections__pb2.CollectionOperationResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/qdrant.Collections/Update',
                request_serializer=collections__pb2.UpdateCollection.SerializeToString,
                response_deserializer=collections__pb2.CollectionOperationResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/qdrant.Collections/Delete',
                request_serializer=collections__pb2.DeleteCollection.SerializeToString,
                response_deserializer=collections__pb2.CollectionOperationResponse.FromString,
                )
        self.UpdateAliases = channel.unary_unary(
                '/qdrant.Collections/UpdateAliases',
                request_serializer=collections__pb2.ChangeAliases.SerializeToString,
                response_deserializer=collections__pb2.CollectionOperationResponse.FromString,
                )


class CollectionsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Get(self, request, context):
        """
        Get detailed information about specified existing collection
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """
        Get list name of all existing collections
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """
        Create new collection with given parameters
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """
        Update parameters of the existing collection
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """
        Drop collection and all associated data
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAliases(self, request, context):
        """
        Update Aliases of the existing collection
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CollectionsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=collections__pb2.GetCollectionInfoRequest.FromString,
                    response_serializer=collections__pb2.GetCollectionInfoResponse.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=collections__pb2.ListCollectionsRequest.FromString,
                    response_serializer=collections__pb2.ListCollectionsResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=collections__pb2.CreateCollection.FromString,
                    response_serializer=collections__pb2.CollectionOperationResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=collections__pb2.UpdateCollection.FromString,
                    response_serializer=collections__pb2.CollectionOperationResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=collections__pb2.DeleteCollection.FromString,
                    response_serializer=collections__pb2.CollectionOperationResponse.SerializeToString,
            ),
            'UpdateAliases': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAliases,
                    request_deserializer=collections__pb2.ChangeAliases.FromString,
                    response_serializer=collections__pb2.CollectionOperationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'qdrant.Collections', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Collections(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Collections/Get',
            collections__pb2.GetCollectionInfoRequest.SerializeToString,
            collections__pb2.GetCollectionInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Collections/List',
            collections__pb2.ListCollectionsRequest.SerializeToString,
            collections__pb2.ListCollectionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Collections/Create',
            collections__pb2.CreateCollection.SerializeToString,
            collections__pb2.CollectionOperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Collections/Update',
            collections__pb2.UpdateCollection.SerializeToString,
            collections__pb2.CollectionOperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Collections/Delete',
            collections__pb2.DeleteCollection.SerializeToString,
            collections__pb2.CollectionOperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateAliases(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Collections/UpdateAliases',
            collections__pb2.ChangeAliases.SerializeToString,
            collections__pb2.CollectionOperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
