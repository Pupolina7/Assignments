import argparse
import random
import threading
import time
from concurrent import futures

import grpc

import raft_pb2 as pb2
import raft_pb2_grpc as pb2_grpc

NODE_ID = None
SERVERS_INFO = {}
SUSPEND = False
STATE = "Follower"
TERM = 0
VOTED = False
UNCOMMITTED_VALUE = 0
COMMITTED_VALUE = 0
ELECTION_TIMEOUT = random.uniform(2.0, 4.0)
APPEND_ENTRIES_TIMEOUT = 0.4
CURRENT_LEADER_ID = None
NODE_STATE_LOCK = threading.Lock()


class Handler(pb2_grpc.RaftNodeServicer):
    def __init__(self):
        super().__init__()

    def AppendEntries(self, request, context):
        global CURRENT_LEADER_ID, STATE, TERM
        with NODE_STATE_LOCK:
            if SUSPEND:
                context.set_details("Server suspended")
                context.set_code(grpc.StatusCode.UNAVAILABLE)
                return pb2.AppendEntriesResponse()

            if request.term < TERM:
                context.set_details("Stale term")
                context.set_code(grpc.StatusCode.OUT_OF_RANGE)
                return pb2.AppendEntriesResponse()

            CURRENT_LEADER_ID = request.leader_id
            STATE = "Follower"
            TERM = request.term
            reset_election_timeout()

            print(f"STATE: {STATE} | TERM: {TERM}")

        return pb2.AppendEntriesResponse(term=TERM, heartbeat_result=True)

    def RequestVote(self, request, context):
        global STATE, TERM, VOTED
        with NODE_STATE_LOCK:
            if SUSPEND:
                context.set_details("Server suspended")
                context.set_code(grpc.StatusCode.UNAVAILABLE)
                return pb2.RequestVoteResponse()

            print(f'RPC[RequestVote] Invoked')
            print(f'\t\tcandidate_id: {request.candidate_id}')
            print(f'\t\tcandidate_term: {request.candidate_term}')

            if request.candidate_term < TERM:
                return pb2.RequestVoteResponse(term=TERM, vote_result=False)

            if request.candidate_term > TERM:
                STATE = "Follower"
                TERM = request.candidate_term
                VOTED = False

            if not VOTED:
                VOTED = True
                print(f"Voted for NODE {request.candidate_id}")
                return pb2.RequestVoteResponse(term=TERM, vote_result=True)
            else:
                return pb2.RequestVoteResponse(term=TERM, vote_result=False)

    def GetLeader(self, request, context):
        global CURRENT_LEADER_ID
        with NODE_STATE_LOCK:
            if SUSPEND:
                context.set_details("Server suspended")
                context.set_code(grpc.StatusCode.UNAVAILABLE)
                return pb2.GetLeaderResponse()
            print(f'RPC[GetLeader] Invoked')
            return pb2.GetLeaderResponse(leader_id=CURRENT_LEADER_ID)

    def AddValue(self, request, context):
        global STATE, UNCOMMITTED_VALUE
        with NODE_STATE_LOCK:
            if SUSPEND:
                context.set_details("Server suspended")
                context.set_code(grpc.StatusCode.UNAVAILABLE)
                return pb2.AddValueResponse()

            print(f'RPC[AddValue] Invoked')
            print(f'\tArgs:')
            print(f'\t\tvalue_to_add: {request.value_to_add}')

            if STATE != "Leader":
                context.set_details("Not a leader")
                context.set_code(grpc.StatusCode.FAILED_PRECONDITION)
                return pb2.AddValueResponse()
            UNCOMMITTED_VALUE += request.value_to_add
            return pb2.AddValueResponse()

    def GetValue(self, request, context):
        global COMMITTED_VALUE
        with NODE_STATE_LOCK:
            if SUSPEND:
                context.set_details("Server suspended")
                context.set_code(grpc.StatusCode.UNAVAILABLE)
                return pb2.GetValueResponse()
            print(f'RPC[GetValue] Invoked')
            return pb2.GetValueResponse(value=COMMITTED_VALUE)

    def Suspend(self, request, context):
        print(f'RPC[Suspend] Invoked')
        global SUSPEND
        SUSPEND = True
        return pb2.SuspendResponse()

    def Resume(self, request, context):
        print(f'RPC[Resume] Invoked')
        global SUSPEND
        SUSPEND = False
        return pb2.ResumeResponse()


def reset_election_timeout():
    global ELECTION_TIMEOUT
    ELECTION_TIMEOUT = random.uniform(2.0, 4.0)


def start_election():
    global STATE, TERM, VOTED
    with NODE_STATE_LOCK:
        STATE = "Candidate"
        TERM += 1
        VOTED = True
        reset_election_timeout()
        print(f"STATE: {STATE} | TERM: {TERM}")


def election_timer():
    global STATE
    while True:
        if STATE == "Follower" and not SUSPEND:
            time.sleep(ELECTION_TIMEOUT)
            start_election()


# ----------------------------- Do not change -----------------------------
def serve():
    print(f'NODE {NODE_ID} | {SERVERS_INFO[NODE_ID]}')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_RaftNodeServicer_to_server(Handler(), server)
    server.add_insecure_port(SERVERS_INFO[NODE_ID])
    try:
        server.start()
        while True:
            server.wait_for_termination()
    except grpc.RpcError as e:
        print(f"Unexpected Error: {e}")
    except KeyboardInterrupt:
        server.stop(grace=10)
        print("Shutting Down...")


def init(node_id):
    global NODE_ID
    NODE_ID = node_id

    with open("config.conf") as f:
        global SERVERS_INFO
        lines = f.readlines()
        for line in lines:
            parts = line.split()
            id, address = parts[0], parts[1]
            SERVERS_INFO[int(id)] = str(address)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("node_id", type=int)
    args = parser.parse_args()

    init(args.node_id)

    serve()
# ----------------------------- Do not change -----------------------------
