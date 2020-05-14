from tool import tool
from tool.MixerChannel import MixerChannel

if __name__ == "__main__":

    other = [
        "chrome",
        "discord",
        "spotify",
        "system",
    ]

    channels = [
        MixerChannel(mapping="master", midi={
            0: "level",
            48: "mute",
            32: "solo",
        }),

        MixerChannel(exceptions=other, midi={
            1: "level",
            49: "mute",
            33: "solo",
        }),

        MixerChannel(mapping="chrome", midi={
            2: "level",
            50: "mute",
            34: "solo",
        }),

        MixerChannel(mapping="spotify", midi={
            3: "level",
            51: "mute",
            35: "solo",
        }),

        MixerChannel(mapping="discord", midi={
            7: "level",
            55: "mute",
            39: "solo",
        }),

        MixerChannel(mapping="media_play_pause", midi={
            41: "keyboard"
        }),
        MixerChannel(mapping="media_previous", midi={
            43: "keyboard"
        }),
        MixerChannel(mapping="media_next", midi={
            44: "keyboard"
        }),
    ]

    tool(channels);
