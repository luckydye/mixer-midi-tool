from tool.AudioInterface import AudioInterface

audio = AudioInterface()

class MixerChannel:

    title = "Channel"
    
    def __init__(self, channel, application, master = False):
        self.channel = channel
        self.application = application
        self.master = master

    def setVolume(self, volume):
        if(self.master):
            audio.setMasterVolume(volume)
        else:
            audio.setProcessVolume(self.application, volume)
