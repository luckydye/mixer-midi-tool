from tool.AudioInterface import AudioInterface

audio = AudioInterface()

class MixerChannel:

    title = "Channel"
    
    def __init__(self, channel, application, master = False, exceptions = []):
        self.channel = channel
        self.application = application
        self.master = master
        self.exceptions = exceptions

    def setVolume(self, volume):
        if(len(self.exceptions) > 0):
            audio.setAllProcessVolumeExcept(self.exceptions, volume)
        else:
            audio.setProcessVolume(self.application, volume)

        if(self.master):
            audio.setMasterVolume(volume)
