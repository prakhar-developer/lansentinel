import unittest
from core.packet import Packet

class TestPacket(unittest.TestCase):
    def test_packet_build_parse(self):
        original_data = b"Hello Packet"
        pkt = Packet(command="MSG", payload=original_data)
        raw = pkt.build()
        parsed = Packet.parse(raw)
        self.assertEqual(parsed.command, "MSG")
        self.assertEqual(parsed.payload, original_data)

if __name__ == '__main__':
    unittest.main()
