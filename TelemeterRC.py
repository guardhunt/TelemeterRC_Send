import socket
import appcodec
from time import sleep

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

    def push(self):
        while 1:
            payload = appcodec.encode()
            self.sendFrame(payload)
            sleep(.01)
    def listen(self):
        while(1):
            frame = self.socket.recv(1500)
            self.decode(frame)

    def decode(self, frame):
        appcodec.decode(frame)
