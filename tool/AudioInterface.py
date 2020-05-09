from __future__ import print_function
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import re
import math

class AudioInterface:

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    master = cast(interface, POINTER(IAudioEndpointVolume))
    sessions = AudioUtilities.GetAllSessions()

    # volume from 0 - 100
    def setMasterVolume(self, newVolume):
        newVolume = (100 - newVolume) / 100
        newVolume = math.pow(newVolume, 2.0)
        newVolume = newVolume * -100

        self.master.SetMasterVolumeLevel(newVolume, None)


    # volume from 0 - 100
    def setProcessVolume(self, processName, newVolume):
        newVolume = (100 - newVolume) / 100
        newVolume = 1 - newVolume

        for session in self.sessions:
            p = re.compile(processName)

            if session.Process and p.match(session.Process.name().lower()):
                volume = session.SimpleAudioVolume
                volume.SetMasterVolume(newVolume, None)
            else:
                continue
