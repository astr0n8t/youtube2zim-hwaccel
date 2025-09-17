from typing import ClassVar

from zimscraperlib.video.config import Config

preset_type = "video"


class VideoWebmHigh(Config):
    """High Quality webm video

    25 constant quality"""

    VERSION = 2

    ext = "webm"
    mimetype = f"{preset_type}/webm"

    options: ClassVar[dict[str, str | None]] = {
        "-vf": "format=qsv,scale_qsv=w=1280:h=720",
        "-codec:v": "vp9_qsv",  # video codec
        "-b:v": "340k",  # Adjust quantizer within min/max to target this bitrate
        "-qmin": "26",  # Reduce the bitrate on very still videos
        "-qmax": "54",  # Increase the bitrate on very busy videos
        "-g": "240",  # Number of frames allowed between keyframes
        "-quality": "good",  # codec preset
        # Encoding speed (compromise between quality and encoding time)
        "-speed": "1",
        "-codec:a": "libvorbis",  # audio codec
        "-b:a": "48k",  # target audio bitrate
        "-ar": "44100",  # audio sampling rate
        "-ac": "2",  # force stereo
    }


class VideoMp4Low(Config):
    """Low Quality mp4 video

    480:h format with height adjusted to keep aspect ratio
    300k video bitrate
    48k audio bitrate
    highly degraded quality (30, 42)"""

    VERSION = 1

    ext = "mp4"
    mimetype = f"{preset_type}/mp4"

    options: ClassVar[dict[str, str | None]] = {
        "-vf": "format=qsv,scale_qsv=w=1280:h=720",
        "-codec:v": "h264_qsv",  # video codec
        "-b:v": "300k",  # target video bitrate
        "-maxrate": "300k",  # max video bitrate
        "-minrate": "300k",  # min video bitrate
        "-qmin": "30",  # min quantizer scale
        "-qmax": "42",  # max quantizer scale
        "-codec:a": "aac",  # audio codec
        "-ar": "44100",  # audio sampling rate
        "-b:a": "48k",  # target audio bitrate
        "-movflags": "+faststart",  # extra flag
        "-ac": "2",  # force stereo
    }
