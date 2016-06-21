import socket

class TelemeterRcDaemon():
    """docstring for TelemeterRcDaemon"""
    def __init__(self, src, dst, type):
        self.src = src
        self.dst = dst
        self.type = type
        self.socket = socket.socket(AF_PACKET, SOCK_RAW)
        self.socket.bind((interface, 0))

    def sendFrame(self, payload):
        assert(len(self.src) == len(self.dst) == 6)
        assert(len(self.type) == 2)
        return self.socket.send(self.src + self.dst + self.type + payload)

    def listen(self):
        while(1):
            frame = self.socket.recv(1500)
            self.decode(frame)

    def decode(self, frame):
        
