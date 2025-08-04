import socket
from core.encryption import encrypt

def send_message(host, port, packet):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    encrypted_data = encrypt(packet.serialize())
    s.sendall(encrypted_data)
    s.close()
