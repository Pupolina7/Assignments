# import argparse
# import socket
# import logging
#
# from threading import Thread
#
# client_port = None
# server_port = None
#
# server_address = ("0.0.0.0", server_port)
# client_address = ("127.0.0.1", client_port)
#
# status = True
#
# logging.basicConfig(filename="messenger.log", filemode='a', level=logging.DEBUG)
#
#
# def await_ack(packet, client_socket, expected_seqno):
#     global client_port
#     global status
#     client_socket.settimeout(1)
#
#     # TODO: finish implementation for receiving acknolwedgement packets, that arrive to client_socket
#     # DO NOT FORGET about placing a log on received packets
#     while True:
#         try:
#             addr, data = packet
#             print(f"Received by the client: {data.decode()}")
#             received_ack_type = data[:1].decode()
#             received_ack_seqno = int(data[2:].decode())
#             if received_ack_seqno != expected_seqno:
#                 continue
#             logging.info(f"{client_socket.getsockname()}: Received [{data.decode()}] from {addr}")
#             break
#         except socket.timeout:
#             client_socket.sendto(packet[1], server_address)
#
#     # logging.info(f"{client_socket.getsockname()}: Received [{data.decode()}] from {addr}")
#
#
# def server_thread_handler():
#     global server_port
#     global status
#
#     user_name = None
#     expected_server_seqno = 0
#
#     with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as server_socket:
#         server_socket.settimeout(2)
#         server_socket.bind(("0.0.0.0", server_port))
#         while status:
#             # Wait for a client message
#             try:
#                 data, addr = server_socket.recvfrom(1024)
#                 logging.info(f"{server_socket.getsockname()}: Received [{data.decode()}] from {addr}")
#             except socket.timeout:
#                 continue
#
#             packet_type, seqno, payload = data.decode().split('|')
#
#             # Handle start packet
#             if packet_type == "s":
#                 # TODO: finish handling "start" packet in "server" part
#                 user_name = payload
#                 reply = f"a|{seqno}".encode()
#                 server_socket.sendto(reply, client_address)
#             # Handle messages
#             elif packet_type == "m":
#                 # TODO: finish handling messages in "server" part
#                 if expected_server_seqno == seqno:
#                     print(f"{user_name}: payload")
#                 reply = f"a|{seqno}".encode()
#                 server_socket.sendto(reply, client_address)
#                 expected_server_seqno = 1 - expected_server_seqno
#
#
#
# def client_handler():
#     global client_port
#     global status
#
#     with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as client_socket:
#         client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 30000)
#         name = input("Enter your user name: ")
#         client_seqno = 0
#         message = input()
#
#         # TODO: Finish impelementation of the "client" part
#         packet = f"s|{client_seqno}|{name}".encode()
#         print(client_address)
#         client_socket.sendto(packet, server_address)
#         packet = client_socket.recvfrom(1024)
#         await_ack(packet, client_socket, (client_seqno + 1) % 2)
#
#         while status:
#             try:
#                 packet = f"m|{client_seqno}|{message}".encode()
#                 client_socket.sendto(packet, server_address)
#                 packet = client_socket.recvfrom(1024)
#                 await_ack(packet, client_socket, (client_seqno + 1) % 2)
#                 client_seqno = 1 - client_seqno
#             except KeyboardInterrupt:
#                 print("Exiting")
#
#
#
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument("server_port", type=int)
#     parser.add_argument("client_port", type=int)
#     args = parser.parse_args()
#
#     client_port = args.client_port
#     server_port = args.server_port
#
#     server_address = ("0.0.0.0", server_port)
#     client_address = ("127.0.0.1", client_port)
#
#     server_thread = Thread(target=server_thread_handler)
#     server_thread.start()
#
#     try:
#         client_handler()
#     except KeyboardInterrupt:
#         print("Exiting")
#         status = False
#         server_thread.join()
#
