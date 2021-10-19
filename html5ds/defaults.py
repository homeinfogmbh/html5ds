"""Default values."""

from enum import Enum

from html5ds.types import Position, Resolution


__all__ = ['Defaults']


class Defaults(Enum):
    """Default configuration values."""

    EXECUTABLE = '/usr/bin/chromium'
    POSITION = Position(0, 0)
    RESOLUTION = Resolution(1920, 1080)
    DISK_CACHE_DIR = '/dev/null'
    VERBOSITY = 1
    URL = 'http://localhost/index.html'
    DISPLAY = ':0'
