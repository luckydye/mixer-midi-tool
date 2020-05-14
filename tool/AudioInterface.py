from __future__ import print_function
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import re
import math

def getMasterEndpoint():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    master = cast(interface, POINTER(IAudioEndpointVolume))
    return master

def getAudioSessions():
    return AudioUtilities.GetAllSessions()

class AudioInterface:

    def __init__(self):
        self.sessions = getAudioSessions()


    def findProcesses(self, processName):
        sessions = []

        for session in self.sessions:
            p = re.compile(processName)

            if session.Process and p.match(session.Process.name().lower()):
                sessions.append(session);
            else:
                continue
            
        return sessions


    def findProcessesExcept(self, processNames):
        sessions = []

        for session in self.sessions:
            if session.Process:
                processName = session.Process.name().lower()

                matched = False

                for appName in processNames:
                    p = re.compile(appName)

                    if p.match(processName):
                        matched = True
                        break;

                if not matched:
                    sessions.append(session)
            
        return sessions


    def setSessionMute(self, value, session):
        volume = session.SimpleAudioVolume
        volume.SetMute(int(value), None)

    def setMasterMute(self, value):
        master = getMasterEndpoint()
        master.SetMute(int(value), None)

    def setSessionVolume(self, value, session):
        volume = session.SimpleAudioVolume
        volume.SetMasterVolume(value, None)


    # 0 or 1
    def setMute(self, value, processName):
        for session in self.findProcesses(processName):
            self.setSessionMute(value, session)

    # 0 or 1
    def setMuteExcept(self, value, processNames):
        for session in self.findProcessesExcept(processNames):
            self.setSessionMute(value, session)

    # volume from 0 - 100
    def setMasterVolume(self, newVolume):
        newVolume = (100 - newVolume) / 100
        newVolume = math.pow(newVolume, 2.0)
        newVolume = newVolume * -100

        master = getMasterEndpoint()
        master.SetMasterVolumeLevel(newVolume, None)

    # volume from 0 - 100
    def setProcessVolume(self, processName, newVolume):
        newVolume = 1 - ((100 - newVolume) / 100)
        for session in self.findProcesses(processName):
            self.setSessionVolume(newVolume, session)

    # volume from 0 - 100
    def setAllProcessVolumeExcept(self, processNames, newVolume):
        newVolume = 1 - ((100 - newVolume) / 100)
        for session in self.findProcessesExcept(processNames):
            self.setSessionVolume(newVolume, session)

