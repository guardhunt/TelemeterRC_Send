import socket
import appcodec
from time import sleep

class TelemeterRcDaemon():
    """docstring for TelemeterRcDaemon"""
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
        self.type = "{:04X}".format(257)
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
            print(payload + " sent")

    def listen(self):
        while(1):
            frame = self.socket.recv(1500)
            if(frame[12:14] == self.type):
                self.decode(frame[14:])

    def decode(self, frame):
        appcodec.decode(frame)
