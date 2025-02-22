# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import movies_pb2 as movies__pb2


class MoviesServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateMovie = channel.unary_unary(
                '/movies.MoviesService/CreateMovie',
                request_serializer=movies__pb2.CreateMovieRequest.SerializeToString,
                response_deserializer=movies__pb2.CreateMovieResponse.FromString,
                )
        self.GetMovie = channel.unary_unary(
                '/movies.MoviesService/GetMovie',
                request_serializer=movies__pb2.GetMovieRequest.SerializeToString,
                response_deserializer=movies__pb2.GetMovieResponse.FromString,
                )
        self.UpdateMovie = channel.unary_unary(
                '/movies.MoviesService/UpdateMovie',
                request_serializer=movies__pb2.UpdateMovieRequest.SerializeToString,
                response_deserializer=movies__pb2.UpdateMovieResponse.FromString,
                )
        self.DeleteMovie = channel.unary_unary(
                '/movies.MoviesService/DeleteMovie',
                request_serializer=movies__pb2.DeleteMovieRequest.SerializeToString,
                response_deserializer=movies__pb2.DeleteMovieResponse.FromString,
                )
        self.GetMovieByActor = channel.unary_unary(
                '/movies.MoviesService/GetMovieByActor',
                request_serializer=movies__pb2.GetMovieByActorRequest.SerializeToString,
                response_deserializer=movies__pb2.GetMovieByActorResponse.FromString,
                )
        self.GetMovieByCategory = channel.unary_unary(
                '/movies.MoviesService/GetMovieByCategory',
                request_serializer=movies__pb2.GetMovieByCategoryRequest.SerializeToString,
                response_deserializer=movies__pb2.GetMovieByCategoryResponse.FromString,
                )


class MoviesServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateMovie(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMovie(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateMovie(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteMovie(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMovieByActor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMovieByCategory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MoviesServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateMovie': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateMovie,
                    request_deserializer=movies__pb2.CreateMovieRequest.FromString,
                    response_serializer=movies__pb2.CreateMovieResponse.SerializeToString,
            ),
            'GetMovie': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMovie,
                    request_deserializer=movies__pb2.GetMovieRequest.FromString,
                    response_serializer=movies__pb2.GetMovieResponse.SerializeToString,
            ),
            'UpdateMovie': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateMovie,
                    request_deserializer=movies__pb2.UpdateMovieRequest.FromString,
                    response_serializer=movies__pb2.UpdateMovieResponse.SerializeToString,
            ),
            'DeleteMovie': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteMovie,
                    request_deserializer=movies__pb2.DeleteMovieRequest.FromString,
                    response_serializer=movies__pb2.DeleteMovieResponse.SerializeToString,
            ),
            'GetMovieByActor': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMovieByActor,
                    request_deserializer=movies__pb2.GetMovieByActorRequest.FromString,
                    response_serializer=movies__pb2.GetMovieByActorResponse.SerializeToString,
            ),
            'GetMovieByCategory': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMovieByCategory,
                    request_deserializer=movies__pb2.GetMovieByCategoryRequest.FromString,
                    response_serializer=movies__pb2.GetMovieByCategoryResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'movies.MoviesService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MoviesService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateMovie(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/movies.MoviesService/CreateMovie',
            movies__pb2.CreateMovieRequest.SerializeToString,
            movies__pb2.CreateMovieResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMovie(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/movies.MoviesService/GetMovie',
            movies__pb2.GetMovieRequest.SerializeToString,
            movies__pb2.GetMovieResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateMovie(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/movies.MoviesService/UpdateMovie',
            movies__pb2.UpdateMovieRequest.SerializeToString,
            movies__pb2.UpdateMovieResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteMovie(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/movies.MoviesService/DeleteMovie',
            movies__pb2.DeleteMovieRequest.SerializeToString,
            movies__pb2.DeleteMovieResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMovieByActor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/movies.MoviesService/GetMovieByActor',
            movies__pb2.GetMovieByActorRequest.SerializeToString,
            movies__pb2.GetMovieByActorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMovieByCategory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/movies.MoviesService/GetMovieByCategory',
            movies__pb2.GetMovieByCategoryRequest.SerializeToString,
            movies__pb2.GetMovieByCategoryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
