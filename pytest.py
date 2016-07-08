import evdev
import time
import struct

class packetState():
    def __init__(self):
        self.device = evdev.InputDevice("/dev/input/event2")
        self.capabilities = self.device.capabilities(verbose=True)
        self.capaRAW = self.device.capabilities(absinfo=False)
        self.config = {}
        self.state = {}

    def build(self):
        """build state dictionary for controller"""

        #build config dictionary by code and name
        for key, value in self.capabilities.items():
            for element in value:
                    if type(element[0]) is tuple:
                        self.config[element[0][1]] = element[0][0]
                    elif type(element[0]) is list:
                        self.config[element[1]] = element[0][0]
                    elif ("SYN" in str(element[0])) or ("FF" in str(element[0])):
                        pass
                    else:
                        self.config[element[1]] = element[0]
                    print(element[0])
                    print(type(element[0]))
        print(self.state)
        print("")
        print(self.config)
        #build state dictionary from raw codes
        for code in self.capaRAW[1]:
            self.state[self.config[code]] = 0

        for code in self.capaRAW[3]:
            self.state[self.config[code]] = 0


        for event in self.device.read_loop():
            if event.type == evdev.ecodes.EV_KEY or event.type == evdev.ecodes.EV_ABS:
                self.update_state(event)
                #print("RAW EVENT: " + str(event))
                #print("CTGZ EVENT: " + str(evdev.categorize(event)))
                #print("EVENT VALUE: " + str(event.value))
                #print("EVENT TYPE: " + str(event.type))
                #print("EVNET CODE: " + str(event.code))
                #print("")

    def update_state(self, event):
        self.state[self.config[event.code]] = event.value
        print(self.state)
        button_state = 0
        button_state = button_state | self.state["BTN_A"]
        button_state = button_state | self.state["BTN_B"] << 1
        button_state = button_state | self.state["BTN_NORTH"] << 2
        button_state = button_state | self.state["BTN_WEST"] << 3
        packet = struct.pack('2hc', self.state["ABS_X"], self.state["ABS_Y"], button_state.to_bytes(1, byteorder="big"))
        print(packet)
        print(struct.unpack('2hc', packet))

def main():
    tool = packetState()
    tool.build()

main()
