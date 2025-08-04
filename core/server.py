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
        try:
            data = conn.recv(4096)
            if data:
                raw = decrypt(data)
                packet = Packet.deserialize(raw)
                print(f"[RECV from {packet.sender}] {packet.payload}")
        except Exception as e:
            logging.error(f"[!] Error handling client {addr}: {str(e)}")
        finally:
            conn.close()

    def start(self):
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            print(f"[✅] Server listening on {self.host}:{self.port}...")
            while True:
                conn, addr = self.server_socket.accept()
                thread = threading.Thread(target=self.handle_client, args=(conn, addr))
                thread.daemon = True
                thread.start()
        except Exception as e:
            logging.error(f"[!] Server error: {str(e)}")


# ✅ Add this block to make it executable as a module
if __name__ == "__main__":
    import argparse
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default="0.0.0.0")
    parser.add_argument('--port', type=int, default=5001)
    args = parser.parse_args()

    print("[🟢] Starting LANSentinel++ Peer Server...")
    server = PeerServer(name="Admin", host=args.host, port=args.port)
    server.start()
