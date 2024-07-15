import grpc
import sys
import chord_pb2 as pb2
import chord_pb2_grpc as pb2_grpc

CHANNELS = [
    "127.0.0.1:5000",
    "127.0.0.1:5001",
    "127.0.0.1:5002",
    "127.0.0.1:5003",
    "127.0.0.1:5004",
    "127.0.0.1:5005",
]


def get_stub(channel):
    """ Create a gRPC stub for the specified channel. """
    channel = grpc.insecure_channel(channel)
    return pb2_grpc.ChordStub(channel)


def main():
    node_channel = None
    while True:
        try:
            inp = input("> ")
            splits = inp.split()
            command = splits[0]

            if command == "connect":
                node_index = int(splits[1])
                node_channel = CHANNELS[node_index]
                print(f"Connected To Node {node_index}")

            elif command == "get_finger_table":
                if not node_channel:
                    print("Error: No node connected.")
                    continue
                stub = get_stub(node_channel)
                response = stub.GetFingerTable(pb2.GetFingerTableMessage())
                print("Finger Table:", response.finger_table)

            elif command == "save":
                if not node_channel:
                    print("Error: No node connected.")
                    continue
                key = splits[1]
                value = " ".join(splits[2:])
                stub = get_stub(node_channel)
                response = stub.SaveData(pb2.SaveDataMessage(key=key, text=value))
                if response.status:
                    print(f"Success, {key} was saved in node {response.node_id}")
                else:
                    print("Failure, key was not saved")

            elif command == "find":
                if not node_channel:
                    print("Error: No node connected.")
                    continue
                key = splits[1]
                stub = get_stub(node_channel)
                response = stub.FindData(pb2.FindDataMessage(key=key))
                if response.data:
                    print(f"Success, {key} was found in node {response.node_id} with data {response.data}")
                else:
                    print("Failure, data was not found")

            elif command == "remove":
                if not node_channel:
                    print("Error: No node connected.")
                    continue
                key = splits[1]
                stub = get_stub(node_channel)
                response = stub.RemoveData(pb2.RemoveDataMessage(key=key))
                if response.status:
                    print(f"Success, {key} was removed from node {response.node_id}")
                else:
                    print("Failure, key was not removed")

            elif command == "quit":
                print("Shutting Down")
                break

            else:
                print("Unrecognized command")

        except KeyboardInterrupt:
            print("Shutting Down")
            sys.exit(0)


if name == "__main__":
    main()