class Peer:
    def __init__(self, name, host, port):
        self.name = name
        self.host = host
        self.port = port
        self.is_connected = False
