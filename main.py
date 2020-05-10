from tool import tool
from tool.MixerChannel import MixerChannel

if __name__ == "__main__":

    channels = [
        MixerChannel(0, "master", True),
        MixerChannel(1, "other", False, [
            "chrome",
            "discord",
            "spotify",
            "system",
        ]),
        MixerChannel(2, "chrome"),
        MixerChannel(3, "discord"),
        MixerChannel(4, "spotify"),
    ]

    tool(channels);
