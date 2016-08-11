import time
from TelemeterRC import  TelemeterRcDaemon
from appcodec import appcodec

def recieve_frame(app, codec):
    while 1:
        packet = app.listen()
        if packet != None:
            packet = codec.decode(packet)
            print(packet)

def main():
    #app = TelemeterRcDaemon("02c309816887","02560a817385")

    app = TelemeterRcDaemon("02560a817385", "02c309816887")
    codec = appcodec()
    recieve_frame(app, codec)

main()

