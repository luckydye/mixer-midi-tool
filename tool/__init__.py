#!/usr/bin/env python3

from tool.MixerChannel import MixerChannel
from tool.MidiInterface import MidiInterface
from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image
import os 

channels = [
    MixerChannel(0, "master", True),
    MixerChannel(1, "other"),
    MixerChannel(2, "chrome"),
    MixerChannel(3, "discord"),
    MixerChannel(4, "spotify"),
]

midiDeviceName = "nanoKONTROL2 4"

def get_icon_image():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return Image.open(dir_path + "\icon.png")


def tool():

    midi = MidiInterface(midiDeviceName, channels)
    midi.start()

    def on_about_clicked():
        print('nothing')

    def on_exit_clicked(icon, item):
        midi.stop()
        trayIcon.stop()

    trayIcon = icon('test', get_icon_image(), menu=menu(
        item('MidiVolumeMixer', on_about_clicked),
        item('Exit', on_exit_clicked),
    ))
    trayIcon.run()
