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
        "-vf": "format=vaapi,hwupload,scale_vaapi=w=1920:h=1080",
        "-codec:v": "vp9_vaapi",  # video codec
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
