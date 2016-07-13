import socket
import appcodec
from time import sleep
from struct import *
import evdev
import os.path

class TelemeterRcDaemon():
    """docstring for TelemeterRcDaemon"""
    def __init__(self, src, dst):
        self.src = bytes(bytearray.fromhex(src))
        self.dst = bytes(bytearray.fromhex(dst))
        self.type = socket.htons(257)
        self.socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
        self.socket.bind(("eth0", 0))
        print("Socket: " + str(self.socket))

    def sendFrame(self, payload):
        assert(len(self.src) == len(self.dst) == 6)
        assert(len(self.type) == 2)
        self.socket.send(self.dst + self.src + self.type + payload)
        print("Frame Sent!")

    def listen(self):
        frame = self.socket.recv(2048)
        if (int.from_bytes(frame[0:5], byteorder=  "little") == 448841499394):
            return frame

    def findController(self):
        devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
        for device in devices:
            if device.name == "Microsoft X-Box 360 pad":
                controller = evdev.InputDevice(device.fn)
        try:
            controller
        except NameError:
            print("No controller found")
            pass
        else:
           print(str(controller.name) + " found")
           return controller
