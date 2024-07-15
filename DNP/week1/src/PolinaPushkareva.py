import socket
import sys
import os

if len(sys.argv) != 3:
    print("Usage: python3 PolinaPushkareva.py <port> <max_clients>")
    sys.exit(1)

port = int(sys.argv[1])
max_clients = int(sys.argv[2])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('0.0.0.0', port)
sock.bind(server_address)
print(f"{server_address}: Listening...")

buffer_size = 20480
connected_clients = {}


def handle_start(mes, client_address):
    parts = mes.split('|')
    if len(parts) != 4 or parts[0] != 's':
        return "Invalid message format."
    _, seqno, filename, filesize = parts
    if len(connected_clients) >= max_clients:
        sock.sendto(f"n|{(int(seqno) + 1) % 2}".encode(), client_address)
    else:
        connected_clients[client_address] = {'filename': filename, 'filesize': int(filesize), 'received': 0, 'part': 0}
        sock.sendto(f"a|{(int(seqno) + 1) % 2}".encode(), client_address)


def handle_data(mes, client_address):
    parts = mes.split('|')
    if len(parts) != 3 or parts[0] != 'd':
        return "Invalid message format."
    _, seqno, data = parts
    if client_address not in connected_clients:
        return "Client not recognized."
    filename = connected_clients[client_address]['filename']
    with open(filename, 'wb') as f:
        f.write(data.encode())
    connected_clients[client_address]['received'] += len(data)
    connected_clients[client_address]['part'] += 1
    print(f"{client_address}: {mes[:4]}chunk{connected_clients[client_address]['part']}")
    sock.sendto(f"a|{(int(seqno) + 1) % 2}".encode(), client_address)
    if connected_clients[client_address]['received'] >= connected_clients[client_address]['filesize']:
        print(f"{client_address}: Received {filename}.")
        del connected_clients[client_address]


try:
    while True:
        data, address = sock.recvfrom(buffer_size)
        message = data.decode()

        if message.startswith('s'):
            print(f"{address}: {message}")
            handle_start(message, address)
        elif message.startswith('d'):
            handle_data(message, address)
        else:
            print("Received an unrecognized message type.")
            break

except Exception as e:
    print(f"An error occurred: {e}")
except KeyboardInterrupt:
    print("Shutting down...")
finally:
    sock.close()
