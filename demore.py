import time
from TelemeterRC import  TelemeterRcDaemon
from appcodec import appcodec

def recieve_frame(app, codec):
    while 1:
        packet = app.listen()
        if packet != None:
            print(packet[14:28])
            packet = codec.decode(packet)
            print(packet)
        time.sleep(0.01)

def main():
    #app = TelemeterRcDaemon("02c309816887","02560a817385")

    app = TelemeterRcDaemon("02560a817385", "02c309816887")
    codec = appcodec()
    recieve_frame(app, codec)

main()

