import grpc
import sys
import zlib
from concurrent import futures
import chord_pb2_grpc as pb2_grpc
import chord_pb2 as pb2

node_ind = int(sys.argv[1])
CHORD = [2, 16, 24, 25, 26, 31]
node_id = CHORD[node_ind]
M = 5
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
succ = -1
pred = -1


def get_target_id(key):
    hash_value = zlib.adler32(key.encode()) & 0xffffffff
    return hash_value % (2 ** M)


def find_successor(target):
    for node in CHORD:
        if node >= target:
            return node
    return CHORD[0]


def find_predecessor(target):
    if target == CHORD[0]:
        return CHORD[-1]
    for i in range(1, len(CHORD)):
        if target == CHORD[i]:
            return CHORD[i - 1]
    for i in range(1, len(CHORD)):
        if target < CHORD[i]:
            return CHORD[i - 1]
    return CHORD[-1]


def populate_finger_table():
    global finger_table, succ, pred
    finger_table = []
    for i in range(M):
        finger_point = (node_id + 2**i) % (2**M)
        successor = find_successor(finger_point)
        finger_table.append(successor)
    succ = find_successor(node_id + 1)
    pred = find_predecessor(node_id)


def get_stub(channel):
    channel = grpc.insecure_channel(channel)
    return pb2_grpc.ChordStub(channel)


class NodeHandler(pb2_grpc.ChordServicer):
    def SaveData(self, request, context):
        key = request.key
        text = request.text
        target_id = get_target_id(key)
        if (pred < node_id and pred < target_id <= node_id) or (pred > node_id and (target_id > pred or target_id <=
                                                                                    node_id)):
            data[key] = text
            print(f"Node {node_id} says: Saved {key}")
            return pb2.SaveDataResponse(status=True, node_id=node_id)
        next_node_id = self.find_closest_preceding_node(target_id)
        print(f"Node {node_id} says: Save from {node_id} to {next_node_id}")
        stub = get_stub(CHANNELS[CHORD.index(next_node_id)])
        return stub.SaveData(pb2.SaveDataMessage(key=key, text=text))

    def RemoveData(self, request, context):
        key = request.key
        target_id = get_target_id(key)
        if (pred < node_id and pred < target_id <= node_id) or (pred > node_id and (target_id > pred or target_id <=
                                                                                    node_id)):
            if key in data:
                del data[key]
                print(f"Node {node_id} says: Removed {key}")
                return pb2.RemoveDataResponse(status=True, node_id=node_id)
            else:
                print(f"Node {node_id} says: Failed to remove {key} (not found)")
                return pb2.RemoveDataResponse(status=False, node_id=node_id)
        next_node_id = self.find_closest_preceding_node(target_id)
        print(f"Node {node_id} says: Remove from {node_id} to {next_node_id}")
        stub = get_stub(CHANNELS[CHORD.index(next_node_id)])
        return stub.RemoveData(pb2.RemoveDataMessage(key=key))

    def FindData(self, request, context):
        key = request.key
        target_id = get_target_id(key)
        if (pred < node_id and pred < target_id <= node_id) or (pred > node_id and (target_id > pred or target_id <=
                                                                                    node_id)):
            if key in data:
                print(f"Node {node_id} says: Found {key}")
                return pb2.FindDataResponse(data=data[key], node_id=node_id)
            else:
                print(f"Node {node_id} says: {key} not found")
                return pb2.FindDataResponse(data="", node_id=node_id)

        next_node_id = self.find_closest_preceding_node(target_id)
        print(f"Node {node_id} says: Find from {node_id} to {next_node_id}")
        stub = get_stub(CHANNELS[CHORD.index(next_node_id)])
        return stub.FindData(pb2.FindDataMessage(key=key))

    def GetFingerTable(self, request, context):
        return pb2.GetFingerTableResponse(finger_table=finger_table)

    def find_closest_preceding_node(self, target_id):
        for i in range(M - 1, -1, -1):
            if node_id < finger_table[i] < target_id:
                return finger_table[i]
        return succ

    def main():
        try:
            populate_finger_table()
            server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
            pb2_grpc.add_ChordServicer_to_server(NodeHandler(), server)
            server_port = 5000 + CHORD.index(node_id)
            server.add_insecure_port(f"127.0.0.1:{server_port}")
            print(f"Node {node_id}\t finger table: {finger_table}")
            server.start()
            server.wait_for_termination()
        except KeyboardInterrupt:
            print("Shutting down")

    if name == "__main__":
        main()