# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import raft_pb2 as raft__pb2

GRPC_GENERATED_VERSION = '1.63.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in raft_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class RaftNodeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AppendEntries = channel.unary_unary(
                '/RaftNode/AppendEntries',
                request_serializer=raft__pb2.AppendEntriesArgs.SerializeToString,
                response_deserializer=raft__pb2.AppendEntriesResponse.FromString,
                _registered_method=True)
        self.RequestVote = channel.unary_unary(
                '/RaftNode/RequestVote',
                request_serializer=raft__pb2.RequestVoteArgs.SerializeToString,
                response_deserializer=raft__pb2.RequestVoteResponse.FromString,
                _registered_method=True)
        self.GetLeader = channel.unary_unary(
                '/RaftNode/GetLeader',
                request_serializer=raft__pb2.GetLeaderArgs.SerializeToString,
                response_deserializer=raft__pb2.GetLeaderResponse.FromString,
                _registered_method=True)
        self.AddValue = channel.unary_unary(
                '/RaftNode/AddValue',
                request_serializer=raft__pb2.AddValueArgs.SerializeToString,
                response_deserializer=raft__pb2.AddValueResponse.FromString,
                _registered_method=True)
        self.GetValue = channel.unary_unary(
                '/RaftNode/GetValue',
                request_serializer=raft__pb2.GetValueArgs.SerializeToString,
                response_deserializer=raft__pb2.GetValueResponse.FromString,
                _registered_method=True)
        self.Suspend = channel.unary_unary(
                '/RaftNode/Suspend',
                request_serializer=raft__pb2.SuspendArgs.SerializeToString,
                response_deserializer=raft__pb2.SuspendResponse.FromString,
                _registered_method=True)
        self.Resume = channel.unary_unary(
                '/RaftNode/Resume',
                request_serializer=raft__pb2.ResumeArgs.SerializeToString,
                response_deserializer=raft__pb2.ResumeResponse.FromString,
                _registered_method=True)


class RaftNodeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AppendEntries(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RequestVote(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLeader(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddValue(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetValue(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Suspend(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Resume(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RaftNodeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AppendEntries': grpc.unary_unary_rpc_method_handler(
                    servicer.AppendEntries,
                    request_deserializer=raft__pb2.AppendEntriesArgs.FromString,
                    response_serializer=raft__pb2.AppendEntriesResponse.SerializeToString,
            ),
            'RequestVote': grpc.unary_unary_rpc_method_handler(
                    servicer.RequestVote,
                    request_deserializer=raft__pb2.RequestVoteArgs.FromString,
                    response_serializer=raft__pb2.RequestVoteResponse.SerializeToString,
            ),
            'GetLeader': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLeader,
                    request_deserializer=raft__pb2.GetLeaderArgs.FromString,
                    response_serializer=raft__pb2.GetLeaderResponse.SerializeToString,
            ),
            'AddValue': grpc.unary_unary_rpc_method_handler(
                    servicer.AddValue,
                    request_deserializer=raft__pb2.AddValueArgs.FromString,
                    response_serializer=raft__pb2.AddValueResponse.SerializeToString,
            ),
            'GetValue': grpc.unary_unary_rpc_method_handler(
                    servicer.GetValue,
                    request_deserializer=raft__pb2.GetValueArgs.FromString,
                    response_serializer=raft__pb2.GetValueResponse.SerializeToString,
            ),
            'Suspend': grpc.unary_unary_rpc_method_handler(
                    servicer.Suspend,
                    request_deserializer=raft__pb2.SuspendArgs.FromString,
                    response_serializer=raft__pb2.SuspendResponse.SerializeToString,
            ),
            'Resume': grpc.unary_unary_rpc_method_handler(
                    servicer.Resume,
                    request_deserializer=raft__pb2.ResumeArgs.FromString,
                    response_serializer=raft__pb2.ResumeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'RaftNode', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RaftNode(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AppendEntries(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/RaftNode/AppendEntries',
            raft__pb2.AppendEntriesArgs.SerializeToString,
            raft__pb2.AppendEntriesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RequestVote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/RaftNode/RequestVote',
            raft__pb2.RequestVoteArgs.SerializeToString,
            raft__pb2.RequestVoteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetLeader(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/RaftNode/GetLeader',
            raft__pb2.GetLeaderArgs.SerializeToString,
            raft__pb2.GetLeaderResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AddValue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/RaftNode/AddValue',
            raft__pb2.AddValueArgs.SerializeToString,
            raft__pb2.AddValueResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetValue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/RaftNode/GetValue',
            raft__pb2.GetValueArgs.SerializeToString,
            raft__pb2.GetValueResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Suspend(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/RaftNode/Suspend',
            raft__pb2.SuspendArgs.SerializeToString,
            raft__pb2.SuspendResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Resume(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/RaftNode/Resume',
            raft__pb2.ResumeArgs.SerializeToString,
            raft__pb2.ResumeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
