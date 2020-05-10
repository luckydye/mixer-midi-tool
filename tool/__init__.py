#!/usr/bin/env python3

from tool.MidiInterface import MidiInterface
from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image
import os 

def get_icon_image():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return Image.open(dir_path + "\icon.png")

midi = None

def tool(channels):

    def startMidiThread(midiDeviceName):
        global midi

        if(midi):
            midi.stop()
            
        midi = MidiInterface(midiDeviceName, channels)
        midi.start()
        return midi

    def on_exit_clicked(icon, item):
        midi.stop()
        trayIcon.stop()

    def set_state(v):
        def inner(icon, item):
            startMidiThread(v)
        return inner

    def get_state(v):
        def inner(item):
            return midi.midiDeviceName == v
        return inner

    def get_menu_items():
        items = [
            item('None', set_state("None"), checked=get_state("None"), radio=True)
        ]

        for port, name in midi.getMidiPorts():
            items.append(
                item(name, set_state(name), checked=get_state(name), radio=True)
            )

        return items


    startMidiThread("nanoKONTROL2")

    trayIcon = icon('MidiVolumeMixer', get_icon_image(), menu=menu(
        item('MIDI Input', menu(get_menu_items)),
        item('Exit', on_exit_clicked)
    ))

    trayIcon.run()
