i
iport socket
import appcodec
from time import sleep
from struct import *


class TelemeterRcDaemon():
    """docstring for TelemeterRcDaemon"""
    def __init__(self, src, dst):
        self.src = bytes(bytearray.fromhex(src))
        self.dst = bytes(bytearray.fromhex(dst))
        self.type = bytes(bytearray.fromhex("0800"))
        self.socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
        self.socket.bind(("eth0", 2))
        print(self.socket)

    def sendFrame(self, payload):
        padding = bytes(64 - len(payload))
        payload = padding + payload
        #self.type = bytes((len(payload)).to_bytes(2, byteorder="big"))
        assert(len(self.src) == len(self.dst) == 6)
        assert(len(self.type) == 2)
        return self.socket.send(self.dst + self.src + self.type + payload)

    def push(self):
        while 1:
            payload = appcodec.encode()
            self.sendFrame(payload)
            sleep(1)
            print(payload.decode("utf-8") + " sent")

    def listen(self):
        while(1):
            frame = self.socket.recv(1500)
            if(frame[12:14] == self.type):
                self.decode(frame[14:])

    def decode(self, frame):
        appcodec.decode(frame)
