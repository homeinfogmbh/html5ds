"""Command line generation."""

from configparser import ConfigParser
from os import environ
from typing import Iterator

from html5ds.config import CONFIG
from html5ds.defaults import DISK_CACHE_DIR
from html5ds.defaults import DISPLAY
from html5ds.defaults import EXECUTABLE
from html5ds.defaults import LOG_TARGET
from html5ds.defaults import POSITION
from html5ds.defaults import RESOLUTION
from html5ds.defaults import URL


__all__ = ['get_command', 'get_environ']


def get_command(config: ConfigParser = CONFIG) -> Iterator[str]:
    """Returns the command to run."""

    yield config.get('webbrowser', 'executable', fallback=EXECUTABLE)

    if config.getboolean('webbrowser', 'kiosk', fallback=True):
        yield '--kiosk'

    if config.getboolean('webbrowser', 'fullscreen', fallback=True):
        yield '--fullscreen'

    width = config.getint('screen', 'width', fallback=RESOLUTION.width)
    height = config.getint('screen', 'height', fallback=RESOLUTION.height)
    yield f'--window-size={width},{height}'

    pos_x = config.getint('screen', 'x', fallback=POSITION.x)
    pos_y = config.getint('screen', 'y', fallback=POSITION.y)
    yield f'--window-position={pos_x},{pos_y}'

    cache = config.get('webbrowser', 'disk_cache_dir', fallback=DISK_CACHE_DIR)
    yield f'--disk-cache-dir={cache}'

    if log_target := config.get('webbrowser', 'logging', fallback=LOG_TARGET):
        yield f'--enable-logging={log_target}'

    if verbosity := config.getint('webbrowser', 'verbosity'):
        yield f'--v={verbosity}'

    if not config.getboolean('webbrowser', 'pinch', fallback=False):
        yield '--disable-pinch'

    if args := config.get('webbrowser', 'options', fallback=None):
        yield from args.split()

    yield config.get('application', 'url', fallback=URL)


def get_environ(config: ConfigParser = CONFIG) -> dict:
    """Returns the environment for the subprocess."""

    return {
        **environ.copy(),
        'DISPLAY': config.get('screen', 'display', fallback=DISPLAY)
    }
