from tool.AudioInterface import AudioInterface
from pynput.keyboard import Key, Controller

audio = AudioInterface()
keyboard = Controller()

class MixerChannel:

    title = "Channel"
    
    def __init__(self, channelType, channel, mapping = None, exceptions = [], toggle = False):
        self.type = channelType
        self.channel = channel
        self.mapping = mapping
        self.exceptions = exceptions
        self.toggle = toggle

    # volume from 0 - 1
    def setValue(self, value):

        if(self.type == "level"):
            value *= 100
            if(len(self.exceptions) > 0):
                audio.setAllProcessVolumeExcept(self.exceptions, value)
            if(self.mapping):
                if(self.mapping == "master"):
                    audio.setMasterVolume(value)
                else:
                    audio.setProcessVolume(self.mapping, value)

        if(self.type == "keyboard" and self.mapping):
            if(not self.toggle and value > 0 or self.toggle):
                if(self.mapping in Key.__dict__):
                    key = Key[self.mapping]
                    keyboard.press(key)
                    keyboard.release(key)
                else:
                    keyboard.press(self.mapping)
                    keyboard.release(self.mapping)
