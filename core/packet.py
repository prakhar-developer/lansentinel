import json

class Packet:
    def __init__(self, command, sender, payload):
        self.command = command
        self.sender = sender
        self.payload = payload

    def serialize(self):
        return json.dumps({
            "command": self.command,
            "sender": self.sender,
            "payload": self.payload
        }).encode()

    @staticmethod
    def deserialize(data):
        obj = json.loads(data.decode())
        return Packet(obj["command"], obj["sender"], obj["payload"])
