import unittest
from core.encryption import AESCipher

class TestEncryption(unittest.TestCase):
    def test_encrypt_decrypt(self):
        key = "mystrongpassword"
        aes = AESCipher(key)
        original = "Hello, secure world!"
        encrypted = aes.encrypt(original)
        decrypted = aes.decrypt(encrypted)
        self.assertEqual(original, decrypted)

if __name__ == '__main__':
    unittest.main()
