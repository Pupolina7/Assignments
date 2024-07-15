import sys
import grpc

import queue_pb2_grpc as q_grpc
import queue_pb2 as q

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 client.py <address>")
        sys.exit(1)
    address = sys.argv[1]
    try:
        with grpc.insecure_channel(address) as channel:
            stub = q_grpc.QueueStub(channel)
            while True:
                command = input("> ").split()
                if command[0] == 'put':
                    print(stub.Put(q.Item(item=command[1])))
                if command[0] == 'peek':
                    out = stub.Peek(q.Empty())
                    if out is not None:
                        print(out)
                    else:
                        print("Queue is empty")
                if command[0] == 'pop':
                    out = stub.Pop(q.Empty())
                    if out is not None:
                        print(out)
                    else:
                        print("Queue is empty")
                if command[0] == 'size':
                    print(stub.Size(q.Empty()))
    except grpc.RpcError as e:
        print(f"gRPC error (code={e.code()}): {e.details()}")
    except KeyboardInterrupt:
        print("Shutting down")
