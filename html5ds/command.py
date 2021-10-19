"""Command line generation."""

from configparser import ConfigParser
from os import environ
from typing import Iterator

from html5ds.config import CONFIG
from html5ds.defaults import Defaults


__all__ = ['get_command', 'get_environ']


def get_command(config: ConfigParser = CONFIG) -> Iterator[str]:
    """Returns the command to run."""

    yield config.get('webbrowser', 'executable', fallback=Defaults.EXECUTABLE)

    if config.getboolean('webbrowser', 'kiosk', fallback=True):
        yield '--kiosk'

    if config.getboolean('webbrowser', 'fullscreen', fallback=True):
        yield '--fullscreen'

    width = config.getint('screen', 'width',
                          fallback=Defaults.RESOLUTION.width)
    height = config.getint(
        'screen', 'height', fallback=Defaults.RESOLUTION.height)
    window_size = ','.join(map(str, (width, height)))
    yield f'--window-size={window_size}'

    posx = config.getint('screen', 'posx', fallback=Defaults.POSITION.x)
    posy = config.getint('screen', 'posy', fallback=Defaults.POSITION.y)
    window_position = ','.join(map(str, (posx, posy)))
    yield f'--window-position={window_position}'

    disk_cache_dir = config.get(
        'webbrowser', 'disk_cache_dir', fallback=Defaults.DISK_CACHE_DIR)
    yield f'--disk-cache-dir={disk_cache_dir}'

    if config.getboolean('webbrowser', 'logging', fallback=True):
        yield '--enable-logging'

    verbosity = config.getint(
        'webbrowser', 'verbosity', fallback=Defaults.VERBOSITY)
    yield f'--v={verbosity}'

    if args := config.get('webbrowser', 'options', fallback=None):
        yield from args.split()

    yield config.get('application', 'url', fallback=Defaults.URL)


def get_environ(config: ConfigParser = CONFIG) -> dict:
    """Returns the environment for the subprocess."""

    env = environ.copy()
    env['DISPLAY'] = config.get('screen', 'display', fallback=Defaults.DISPLAY)
    return env
