"""Default values."""

from html5ds.types import Position, Resolution


__all__ = ['Defaults']


class Defaults:     # pylint: disable=R0903
    """Default configuration values."""

    __slots__ = ()

    EXECUTABLE: str = '/usr/bin/chromium'
    POSITION: Position = Position(0, 0)
    RESOLUTION: Resolution = Resolution(1920, 1080)
    DISK_CACHE_DIR: str = '/dev/null'
    VERBOSITY: int = 1
    URL: str = 'http://localhost/index.html'
    DISPLAY: str = ':0'
