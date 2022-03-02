"""Default values."""

from html5ds.types import Position, Resolution


__all__ = [
    'DISK_CACHE_DIR',
    'DISPLAY',
    'EXECUTABLE',
    'LOG_TARGET',
    'POSITION',
    'RESOLUTION',
    'URL'
]


DISK_CACHE_DIR: str = '/dev/null'
DISPLAY: str = ':0'
EXECUTABLE: str = '/usr/bin/chromium'
LOG_TARGET: str = 'stderr'
POSITION: Position = Position(0, 0)
RESOLUTION: Resolution = Resolution(1920, 1080)
URL: str = 'http://localhost/index.html'
