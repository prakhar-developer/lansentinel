import socket
import threading
import logging
from core.packet import Packet
from core.encryption import decrypt

class PeerServer:
    def __init__(self, name, host, port):
        self.name = name
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def handle_client(self, conn, addr):
        logging.info(f"[+] Incoming connection from {addr}")
        data = conn.recv(4096)
        if data:
            raw = decrypt(data)
            packet = Packet.deserialize(raw)
            print(f"[RECV from {packet.sender}] {packet.payload}")
        conn.close()

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"[Server Listening] on {self.host}:{self.port}")
        while True:
            conn, addr = self.server_socket.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
