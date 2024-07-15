# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import tic_tac_toe_pb2 as tic__tac__toe__pb2


class TicTacToeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateGame = channel.unary_unary(
                '/TicTacToe/CreateGame',
                request_serializer=tic__tac__toe__pb2.CreateGameRequest.SerializeToString,
                response_deserializer=tic__tac__toe__pb2.Game.FromString,
                )
        self.GetGame = channel.unary_unary(
                '/TicTacToe/GetGame',
                request_serializer=tic__tac__toe__pb2.GetGameRequest.SerializeToString,
                response_deserializer=tic__tac__toe__pb2.Game.FromString,
                )
        self.MakeMove = channel.unary_unary(
                '/TicTacToe/MakeMove',
                request_serializer=tic__tac__toe__pb2.MakeMoveRequest.SerializeToString,
                response_deserializer=tic__tac__toe__pb2.Game.FromString,
                )


class TicTacToeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateGame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetGame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MakeMove(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TicTacToeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateGame': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateGame,
                    request_deserializer=tic__tac__toe__pb2.CreateGameRequest.FromString,
                    response_serializer=tic__tac__toe__pb2.Game.SerializeToString,
            ),
            'GetGame': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGame,
                    request_deserializer=tic__tac__toe__pb2.GetGameRequest.FromString,
                    response_serializer=tic__tac__toe__pb2.Game.SerializeToString,
            ),
            'MakeMove': grpc.unary_unary_rpc_method_handler(
                    servicer.MakeMove,
                    request_deserializer=tic__tac__toe__pb2.MakeMoveRequest.FromString,
                    response_serializer=tic__tac__toe__pb2.Game.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TicTacToe', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TicTacToe(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateGame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TicTacToe/CreateGame',
            tic__tac__toe__pb2.CreateGameRequest.SerializeToString,
            tic__tac__toe__pb2.Game.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetGame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TicTacToe/GetGame',
            tic__tac__toe__pb2.GetGameRequest.SerializeToString,
            tic__tac__toe__pb2.Game.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MakeMove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TicTacToe/MakeMove',
            tic__tac__toe__pb2.MakeMoveRequest.SerializeToString,
            tic__tac__toe__pb2.Game.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
