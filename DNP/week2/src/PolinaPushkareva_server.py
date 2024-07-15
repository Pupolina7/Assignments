import socket
import threading
import random


def handle_client(client_socket):
    randoms = [random.randint(-1 * (10 ** 10 - 1), 10 ** 10 - 1) for _ in range(250000)]
    numbers = ','.join(map(str, randoms))
    client_socket.send(numbers.encode())
    client_socket.close()


SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((SERVER_IP, SERVER_PORT))
sock.listen()
print(f"Listening on {SERVER_IP}:{SERVER_PORT}")
try:
    while True:
        clientSock, clientAddr = sock.accept()
        print(f"Sent a file to {clientAddr}")
        clientThread = threading.Thread(target=handle_client, args=(clientSock,))
        clientThread.start()
except KeyboardInterrupt:
    print("Shutting down...")
    sock.close()
