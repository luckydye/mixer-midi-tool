from tool.AudioInterface import AudioInterface
from pynput.keyboard import Key, Controller

audio = AudioInterface()
keyboard = Controller()

class MixerChannel:

    title = "Channel"
    
    def __init__(self, midi = {}, mapping = None, exceptions = [], toggle = False):
        self.mapping = mapping
        self.exceptions = exceptions
        self.toggle = toggle
        self.solo = 0.0
        self.mute = 0.0
        self.midi = midi

    def setSolo(self, value):
        self.solo = value

    def setMute(self, value):
        if(self.mapping == "master"):
            audio.setMasterMute(value);
        else:
            if(len(self.exceptions) > 0):
                audio.setMuteExcept(value, self.exceptions)
            else:
                audio.setMute(value, self.mapping);

    def setLevel(self, value):
        value *= 100
        if(len(self.exceptions) > 0):
            audio.setAllProcessVolumeExcept(self.exceptions, value)
        if(self.mapping):
            if(self.mapping == "master"):
                audio.setMasterVolume(value)
            else:
                audio.setProcessVolume(self.mapping, value)

    def keyboardShortcut(self, value):
        if(not self.toggle and value > 0 or self.toggle):
            if(self.mapping in Key.__dict__):
                key = Key[self.mapping]
                keyboard.press(key)
                keyboard.release(key)
            else:
                keyboard.press(self.mapping)
                keyboard.release(self.mapping)

    # volume from 0 - 1
    def setValue(self, value, channel):
        msgType = self.midi[channel]

        if(msgType == "solo"):
            self.setSolo(value)

        if(msgType == "mute"):
            self.mute = value
            self.setMute(value)

        if(msgType == "level"):
            self.setLevel(value)

        if(msgType == "keyboard" and self.mapping):
            self.keyboardShortcut(value)