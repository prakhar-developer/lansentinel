from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

# 🔐 Constants
SECRET_KEY = b"12345678901234567890123456789012"  # 32 bytes for AES-256
IV = b"1234567890123456"                          # 16 bytes for AES CBC

def encrypt(data: bytes) -> bytes:
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, IV)
    padded = pad(data, AES.block_size)
    encrypted = cipher.encrypt(padded)
    return base64.b64encode(encrypted)

def decrypt(enc_data: bytes) -> bytes:
    encrypted = base64.b64decode(enc_data)
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, IV)
    decrypted = cipher.decrypt(encrypted)
    return unpad(decrypted, AES.block_size)
