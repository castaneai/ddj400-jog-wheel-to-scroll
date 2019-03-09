import sys
import rtmidi
from pynput.mouse import Controller

mouse = Controller()
midiin = rtmidi.RtMidiIn()


def on_message(midi: rtmidi.MidiMessage):
    if midi.isController() and midi.getControllerNumber() in [33, 35]:
        if midi.getControllerValue() == 65:
            mouse.scroll(0, -1)
        elif midi.getControllerValue() == 63:
            mouse.scroll(0, 1)


device_name = midiin.getPortName(0)
if device_name != "DDJ-400":
    print("DDJ-400 port not found")
    sys.exit(1)

midiin.openPort(0)
while True:
    m = midiin.getMessage(500)
    if m:
        on_message(m)
