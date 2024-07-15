import sys
from concurrent import futures
from queue import Queue

import grpc

import queue_pb2_grpc as q_grpc
import queue_pb2 as q

maxsize = None


class QueueServicer(q_grpc.QueueServicer):
    def __init__(self):
        self.queue = Queue(maxsize=int(maxsize))

    def Put(self, request, context):
        self.queue.put(request.item)
        return self.queue.full()

    def Peek(self, request, context):
        if self.queue.empty():
            return None
        return self.queue.queue[0]

    def Pop(self, request, context):
        if self.queue.empty():
            return None
        return self.queue.get()

    def Size(self, request, context):
        return self.queue.qsize()


if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            print("Usage: python3 server.py <port> <size>")
            sys.exit(1)
        port = sys.argv[1]
        maxsize = sys.argv[2]
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        q_grpc.add_QueueServicer_to_server(QueueServicer(), server)
        server.add_insecure_port('[::]:{}'.format(port))
        server.start()
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("Exiting...")
