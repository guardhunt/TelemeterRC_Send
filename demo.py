from TelemeterRC import TelemeterRcDaemon
from appcodec import appcodec
import netifaces
import evdev
from time import sleep

def run_app(app, packet):
    while 1:
        print ("While loop")
        app.sendFrame(packet.build())
        sleep(0.01)

def main():
    #app = TelemeterRcDaemon("02560a817385", "02c309816887")
    app = TelemeterRcDaemon("02560a817385", "02c309816887")
    packet = appcodec()
    print('before run_app')
    run_app(app, packet)

main()
