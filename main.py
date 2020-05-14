from tool import tool
from tool.MixerChannel import MixerChannel

if __name__ == "__main__":

    channels = [
        MixerChannel("level", 0, mapping="master"),
        MixerChannel("mute", 48, mapping="master"),
        MixerChannel("level", 1, exceptions=[
            "chrome",
            "discord",
            "spotify",
            "system",
        ]),
        MixerChannel("mute", 49, exceptions=[
            "chrome",
            "discord",
            "spotify",
            "system",
        ]),
        MixerChannel("level", 2, mapping="chrome"),
        MixerChannel("mute", 50, mapping="chrome"),
        MixerChannel("level", 3, mapping="spotify"),
        MixerChannel("mute", 51, mapping="spotify"),
        MixerChannel("level", 7, mapping="discord"),
        MixerChannel("mute", 55, mapping="discord"),
        MixerChannel("keyboard", 41, mapping="media_play_pause"),
        MixerChannel("keyboard", 43, mapping="media_previous"),
        MixerChannel("keyboard", 44, mapping="media_next"),
    ]

    tool(channels);
