import sys
import fileinput
import io
import struct
import time

def decode(payload):
    """do stuff with frame, generate output"""
    print(payload.decode('latin-1'))

def encode():
    """encode payload from sensors"""

    stream = open('/dev/input/event2', buffering= -1, encoding= ('latin-1'))

    line = stream.readline(16)

    line = line.encode('utf-8')
    return line

    #infile_path = "/dev/input/event2"

    #FORMAT = 'llHHI'
    #EVENT_SIZE = struct.calcsize(FORMAT)

    #in_file = open(infile_path, "rb")

    #event = in_file.read(EVENT_SIZE)


    #(extra, tv_sec, tv_usec, type, code, value) = struct.unpack(FORMAT, event)

    #if type != 0 or code != 0 or value != 0:
    #    return("Event type %u, code %u, value %u at $d.$d" % \
    #        (type, code, value, tv_sec, tv_usec))
    #else:
    #    return("==================================")
