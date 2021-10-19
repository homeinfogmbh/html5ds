"""Launch HTML5-based digital signage applications in a web browser."""

from configparser import ConfigParser
from logging import INFO, basicConfig
from os import environ
from subprocess import run
from typing import Iterator

from html5ds.config import CONFIG, load
from html5ds.defaults import Defaults
from html5ds.logging import FORMAT, LOGGER


__all__ = ['get_command', 'get_environ', 'main']


def get_command(config: ConfigParser = CONFIG) -> Iterator[str]:
    """Returns the command to run."""

    yield config.get(
        'webbrowser', 'executable', fallback=Defaults.EXECUTABLE.value)

    if config.getboolean('webbrowser', 'kiosk', fallback=True):
        yield '--kiosk'

    if config.getboolean('webbrowser', 'fullscreen', fallback=True):
        yield '--fullscreen'

    width = config.getint('screen', 'width',fallback=Defaults.RESOLUTION.value.width)
    height = config.getint(
        'screen', 'height', fallback=Defaults.RESOLUTION.value.height)
    window_size = ','.join(map(str, (width, height)))
    yield f'--window-size={window_size}'

    posx = config.getint('screen', 'posx', fallback=Defaults.POSITION.value.x)
    posy = config.getint('screen', 'posy', fallback=Defaults.POSITION.value.y)
    window_position = ','.join(map(str, (posx, posy)))
    yield f'--window-position={window_position}'

    disk_cache_dir = config.get(
        'webbrowser', 'disk_cache_dir', fallback=Defaults.DISK_CACHE_DIR.value)
    yield f'--disk-cache-dir={disk_cache_dir}'

    if config.getboolean('webbrowser', 'logging', fallback=True):
        yield '--enable-logging'

    verbosity = config.getint(
        'webbrowser', 'verbosity', fallback=Defaults.VERBOSITY.value)
    yield f'--v={verbosity}'

    if args := config.get('webbrowser', 'options', fallback=None):
        yield from args.split()

    yield config.get('application', 'url', fallback=Defaults.URL.value)


def get_environ(config: ConfigParser = CONFIG) -> dict:
    """Returns the environment for the subprocess."""

    env = environ.copy()
    env['DISPLAY'] = config.get(
        'screen', 'display', fallback=Defaults.DISPLAY.value)
    return env


def main() -> int:
    """Runs the program."""

    basicConfig(format=FORMAT, level=INFO)
    load()
    command = tuple(get_command())
    LOGGER.info('Running: %s', command)
    env = get_environ()
    LOGGER.info('Environment: %s', env)
    completed_process = run(command, env=env, check=False)
    return completed_process.returncode
