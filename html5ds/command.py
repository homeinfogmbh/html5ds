"""Command line generation."""

from configparser import ConfigParser
from os import environ
from typing import Iterator

from html5ds.config import CONFIG
from html5ds.defaults import DISK_CACHE_DIR
from html5ds.defaults import DISPLAY
from html5ds.defaults import EXECUTABLE
from html5ds.defaults import POSITION
from html5ds.defaults import RESOLUTION
from html5ds.defaults import URL
from html5ds.defaults import VERBOSITY


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

    posx = config.getint('screen', 'posx', fallback=POSITION.x)
    posy = config.getint('screen', 'posy', fallback=POSITION.y)
    yield f'--window-position={posx},{posy}'

    cache = config.get('webbrowser', 'disk_cache_dir', fallback=DISK_CACHE_DIR)
    yield f'--disk-cache-dir={cache}'

    if target := config.getboolean('webbrowser', 'logging', fallback='stderr'):
        yield f'--enable-logging={target}'

    verbosity = config.getint('webbrowser', 'verbosity', fallback=VERBOSITY)
    yield f'--v={verbosity}'

    if args := config.get('webbrowser', 'options', fallback=None):
        yield from args.split()

    yield config.get('application', 'url', fallback=URL)


def get_environ(config: ConfigParser = CONFIG) -> dict:
    """Returns the environment for the subprocess."""

    env = environ.copy()
    env['DISPLAY'] = config.get('screen', 'display', fallback=DISPLAY)
    return env
