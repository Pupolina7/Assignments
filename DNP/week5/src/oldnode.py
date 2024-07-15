import grpc
import sys
import zlib
from concurrent import futures
import chord_pb2_grpc as pb2_grpc
import chord_pb2 as pb2

node_id = int(sys.argv[1])

CHORD = [2, 16, 24, 25, 26, 31]
CHANNELS = [
    "127.0.0.1:5000",
    "127.0.0.1:5001",
    "127.0.0.1:5002",
    "127.0.0.1:5003",
    "127.0.0.1:5004",
    "127.0.0.1:5005",
]

data = {}
finger_table = []

M = 5
# id = -1
# succ = -1
# pred = -1


# def populate_finger_table(id):
#     def find_sucssessor(target):
#         return
#
#     def find_predecessor(target):
#         return
#
#     return
def populate_finger_table(id_node):
    global finger_table
    for i in range(M):
        finger_table.append((id_node + 2**i) % (2**M))


def get_stub(channel):
    channel = grpc.insecure_channel(channel)
    return pb2_grpc.ChordStub(channel)


def get_target_id(key):
    hash_value = zlib.adler32(key.encode())
    return hash_value % (2 ** M)


def save(key, text):
    target_id = get_target_id(key)
    if target_id <= int(node_id):
        data[key] = text
        return node_id
    else:
        successor_channel = CHANNELS[(node_id + 1) % len(CHANNELS)]
        stub = get_stub(successor_channel)
        return stub.SaveData(pb2.SaveDataMessage(key=key, text=text)).node_id


def remove(key):
    if key in data:
        del data[key]
        return node_id
    else:
        successor_channel = CHANNELS[(node_id + 1) % len(CHANNELS)]
        stub = get_stub(successor_channel)
        return stub.RemoveData(pb2.RemoveDataMessage(key=key)).node_id


def find(key):
    if key in data:
        return data[key], node_id
    else:
        successor_channel = CHANNELS[(node_id + 1) % len(CHANNELS)]
        stub = get_stub(successor_channel)
        return stub.FindData(pb2.FindDataMessage(key=key)).data, stub.FindData(pb2.FindDataMessage(key=key)).node_id


class NodeHandler(pb2_grpc.ChordServicer):
    def SaveData(self, request, context):
        id_node = save(request.key, request.text)
        return pb2.SaveDataResponse(node_id=id_node)
        # reply = {}
        # return pb2.SaveDataResponse(**reply)

    def RemoveData(self, request, context):
        id_node = remove(request.key)
        return pb2.RemoveDataResponse(node_id=id_node)
        # reply = {}
        # return pb2.RemoveDataResponse(**reply)

    def FindData(self, request, context):
        data_found, id_node = find(request.key)
        return pb2.FindDataResponse(data=data_found, node_id=id_node)
        # reply = {}
        # return pb2.FindDataResponse(**reply)

    def GetFingerTable(self, request, context):
        global finger_table
        return pb2.GetFingerTableResponse(finger_table=[pb2.FingerTableEntry(node_id=id_node) for id_node in finger_table])
        # reply = {}
        # return pb2.GetFingerTableResponse(**reply)


if __name__ == "__main__":
    node_port = str(5000 + node_id)
    node = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ChordServicer_to_server(NodeHandler(), node)
    node.add_insecure_port("127.0.0.1:" + node_port)
    node.start()

    try:
        node.wait_for_termination()
    except KeyboardInterrupt:
        print("Shutting down...")
