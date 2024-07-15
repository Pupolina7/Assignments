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
id = -1
succ = -1
pred = -1


def populate_finger_table(id_node):
    global finger_table, succ, pred
    finger_table = []
    finger_table = [find_successor((id_node + 2 ** i) % (2 ** M)) for i in range(M)]
    succ = find_successor(CHORD[node_id] + 1)
    pred = find_predecessor(CHORD[node_id])


def find_successor(target):
    for n in CHORD:
        if n >= target:
            return n
    return CHORD[0]


def find_predecessor(target):
    try:
        idx = CHORD.index(target)
        return CHORD[idx - 1]
    except:
        for num in CHORD:
            if num > target:
                idx = CHORD.index(num)
                return CHORD[idx - 1]
    return CHORD[-1]


def get_stub(channel):
    channel = grpc.insecure_channel(channel)
    return pb2_grpc.ChordStub(channel)


def get_target_id(key):
    hash_value = zlib.adler32(key.encode())
    return hash_value % (2 ** M)


def preceding_node(target):
    closest_node = succ
    for finger_node in reversed(finger_table):
        if CHORD[node_id] < finger_node < target:
            closest_node = finger_node
            break
    return closest_node


def save(key, text):
    target_id = get_target_id(key)
    if (pred < CHORD[node_id] and pred < target_id <= CHORD[node_id]) or (
            pred > CHORD[node_id] and (target_id > pred or target_id <= CHORD[node_id])):
        data[key] = text
        print(f"Node {CHORD[node_id]} says: Saved {key}")
        return CHORD[node_id]
    return -1


def remove(key):
    target_id = get_target_id(key)
    if (pred < CHORD[node_id] and pred < target_id <= CHORD[node_id]) or (
            pred > CHORD[node_id] and (target_id > pred or target_id <= CHORD[node_id])):
        if key in data:
            del data[key]
            print(f"Node {CHORD[node_id]} says: Removed {key}")
            removed = True
        else:
            removed = False
        return CHORD[node_id], removed
    return -1


def find(key):
    target_id = get_target_id(key)
    if (pred < CHORD[node_id] and pred < target_id <= CHORD[node_id]) or (
            pred > CHORD[node_id] and (target_id > pred or target_id <= CHORD[node_id])):
        if key in data:
            print(f"Node {CHORD[node_id]} says: Found {key}")
            return data[key]
        else:
            return ""
    return -1


class NodeHandler(pb2_grpc.ChordServicer):
    def SaveData(self, request, context):
        id_node = save(request.key, request.text)
        if id_node == -1:
            target_id = get_target_id(request.key)
            next_node = preceding_node(target_id)
            print(f"Node {CHORD[node_id]} says: Saved from {CHORD[node_id]} to {next_node}")
            stub = get_stub(CHANNELS[CHORD.index(next_node)])
            return stub.SaveData(pb2.SaveDataMessage(key=request.key, text=request.text))
        return pb2.SaveDataResponse(status=True, node_id=id_node)

    def RemoveData(self, request, context):
        id_node, removed = remove(request.key)
        if id_node == -1:
            target_id = get_target_id(request.key)
            next_node = preceding_node(target_id)
            print(f"Node {CHORD[node_id]} says: Remove from {CHORD[node_id]} to {next_node}")
            stub = get_stub(CHANNELS[CHORD.index(next_node)])
            return stub.RemoveData(pb2.RemoveDataMessage(key=request.key))
        return pb2.RemoveDataResponse(status=removed, node_id=id_node)

    def FindData(self, request, context):
        found_data = find(request.key)
        if found_data == -1:
            target_id = get_target_id(request.key)
            next_node = preceding_node(target_id)
            print(f"Node {CHORD[node_id]} says: Find from {CHORD[node_id]} to {next_node}")
            stub = get_stub(CHANNELS[CHORD.index(next_node)])
            return stub.FindData(pb2.FindDataMessage(key=request.key))
        return pb2.FindDataResponse(data=found_data, node_id=CHORD[node_id])

    def GetFingerTable(self, request, context):
        return pb2.GetFingerTableResponse(finger_table=finger_table)


if __name__ == "__main__":
    node_port = 5000 + node_id
    populate_finger_table(CHORD[node_id])
    node = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ChordServicer_to_server(NodeHandler(), node)
    node.add_insecure_port("127.0.0.1:" + str(node_port))
    node.start()
    print(f"Node {CHORD[node_id]} finger table {finger_table}")

    try:
        node.wait_for_termination()
    except KeyboardInterrupt:
        print("Shutting down...")
