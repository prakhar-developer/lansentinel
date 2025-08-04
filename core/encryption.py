from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

SECRET_KEY = b"12345678901234567890123456789012"  # 32 bytes
IV = b"1234567890123456"  # 16 bytes

def pad(s):
    return s + (16 - len(s) % 16) * chr(16 - len(s) % 16)

def unpad(s):
    return s[:-ord(s[-1])]

def encrypt(data):
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, IV)
    return base64.b64encode(cipher.encrypt(pad(data.decode()).encode()))

def decrypt(enc_data):
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, IV)
    return unpad(cipher.decrypt(base64.b64decode(enc_data)).decode())
