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
        "-vf": "format=nv12,hwupload",
        "-codec:v": "vp9_vaapi",  # video codec
        "-global_quality": "50",
        "-bf": "4",
        "-bsf:v": "vp9_raw_reorder,vp9_superframe",
        "-codec:a": "libvorbis",  # audio codec
        "-b:a": "48k",  # target audio bitrate
        "-ar": "44100",  # audio sampling rate
        "-ac": "2",  # force stereo
    }
