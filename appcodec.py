import sys
import fileinput
import io
import struct
import time
import evdev
from evdev import InputDevice, categorize, ecodes
def decode(payload):
    """do stuff with frame, generate output"""
    print(payload.decode('latin-1'))

def encode(controller):
    """encode payload from sensors"""

    for event in controller.read_loop():
        print("test")
        return (categorize(event))

class Appcodec:

    def __init__
