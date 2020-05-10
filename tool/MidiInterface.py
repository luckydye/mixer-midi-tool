import sys
import time
import threading
import re
from rtmidi.midiutil import open_midiinput
from rtmidi import (API_LINUX_ALSA, API_MACOSX_CORE, API_RTMIDI_DUMMY,
                    API_UNIX_JACK, API_WINDOWS_MM, MidiIn, MidiOut,
                    API_UNSPECIFIED, get_compiled_api)

apis = {
    API_MACOSX_CORE: "macOS (OS X) CoreMIDI",
    API_LINUX_ALSA: "Linux ALSA",
    API_UNIX_JACK: "Jack Client",
    API_WINDOWS_MM: "Windows MultiMedia",
    API_RTMIDI_DUMMY: "RtMidi Dummy"
}


class MidiInputHandler(object):
    def __init__(self, port, channels):
        self.port = port
        self.channels = channels
        self._wallclock = time.time()

    def __call__(self, event, data=None):
        message, deltatime = event
        self._wallclock += deltatime
        self.handleMessage(message)

    def handleMessage(self, message):
        cc = message[1]
        velocity = message[2]

        for channel in self.channels:
            if(channel.channel == cc):
                volume = velocity / 127 * 100
                channel.setVolume(volume)


class MidiInterface(threading.Thread):

    def __init__(self, midiDeviceName, channels):
        threading.Thread.__init__(self)
        self.midiDeviceName = midiDeviceName
        self.channels = channels

    def run(self):
        self.kill = False
        if(self.midiDeviceName != "None"):
            self.bindMidiChannels(self.midiDeviceName, self.channels)

    def stop(self):
        self.kill = True

    def getMidiPorts(self):
        available_apis = get_compiled_api()

        for api, api_name in sorted(apis.items()):
            if api in available_apis:
                for name, class_ in (("input", MidiIn), ("output", MidiOut)):
                    try:
                        midi = class_(api)
                        ports = midi.get_ports()
                    except StandardError as exc:
                        print("Could not probe MIDI %s ports: %s" % (name, exc))
                        continue

                    if not ports:
                        print("No MIDI %s ports found." % name)
                    else:
                        return enumerate(ports)

                    print('')
                    del midi
    
    def getMidiPortByName(self, deviceName):
        p = re.compile(deviceName)

        for port, name in self.getMidiPorts():
            if(p.match(name)):
                return port;

    def bindMidiChannels(self, deviceName, channels):
        devicePort = self.getMidiPortByName(deviceName)

        try:
            midiin, port_name = open_midiinput(devicePort)
            self.midiDeviceName = port_name
            print("Useing MIDI device: " + port_name)
        except (EOFError, KeyboardInterrupt):
            sys.exit()

        midiin.set_callback(MidiInputHandler(port_name, channels))

        print("Listening for MIDI input...")
        try:
            while not self.kill:
                time.sleep(1)
        except KeyboardInterrupt:
            print('')
        finally:
            print("Exit " + deviceName)
            if(midiin):
                midiin.close_port()
