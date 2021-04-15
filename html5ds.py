"""Launch HTML5-based digital signage applications in a web browser."""

from configparser import ConfigParser
from logging import INFO, basicConfig, getLogger
from os import environ
from pathlib import Path
from subprocess import run
from typing import Iterator


__all__ = [
    'CONFIG',
    'CONFIG_FILE',
    'DEFAULT_EXECUTABLE',
    'DEFAULT_WIDTH',
    'DEFAULT_HEIGHT',
    'DEFAULT_POSX',
    'DEFAULT_POSY',
    'DEFAULT_DISK_CACHE_DIR',
    'DEFAULT_VERBOSITY',
    'DEFAULT_URL',
    'DEFAULT_DISPLAY',
    'load_config',
    'get_command',
    'main'
]


CONFIG = ConfigParser()
CONFIG_FILE = Path('/etc/html5ds.conf')
DEFAULT_EXECUTABLE = '/usr/bin/chromium'
DEFAULT_WIDTH = 1920
DEFAULT_HEIGHT = 1080
DEFAULT_POSX = 0
DEFAULT_POSY = 0
DEFAULT_DISK_CACHE_DIR = '/dev/null'
DEFAULT_VERBOSITY = 1
DEFAULT_URL = 'http://localhost/index.html'
DEFAULT_DISPLAY = ':0'
FORMAT = '[%(levelname)s] %(name)s: %(message)s'
LOGGER = getLogger('html5ds')


def load_config(file: Path = CONFIG_FILE) -> list[str]:
    """Loads the config file."""

    return CONFIG.read(file)


def get_command(config: ConfigParser = CONFIG) -> Iterator[str]:
    """Returns the command to run."""

    yield config.get('webbrowser', 'executable', fallback=DEFAULT_EXECUTABLE)

    if config.getboolean('webbrowser', 'kiosk', fallback=True):
        yield '--kiosk'

    if config.getboolean('webbrowser', 'fullscreen', fallback=True):
        yield '--fullscreen'

    width = config.getint('screen', 'width', fallback=DEFAULT_WIDTH)
    height = config.getint('screen', 'height', fallback=DEFAULT_HEIGHT)
    window_size = ','.join(map(str, (width, height)))
    yield f'--window-size={window_size}'

    posx = config.getint('screen', 'posx', fallback=DEFAULT_POSX)
    posy = config.getint('screen', 'posy', fallback=DEFAULT_POSY)
    window_position = ','.join(map(str, (posx, posy)))
    yield f'--window-position={window_position}'

    disk_cache_dir = config.get('webbrowser', 'disk_cache_dir',
                                fallback=DEFAULT_DISK_CACHE_DIR)
    yield f'--disk-cache-dir={disk_cache_dir}'

    if config.getboolean('webbrowser', 'logging', fallback=True):
        yield '--enable-logging'

    verbosity = config.getint('webbrowser', 'verbosity',
                              fallback=DEFAULT_VERBOSITY)
    yield f'--v={verbosity}'

    if args := config.get('webbrowser', 'options', fallback=None):
        yield from args.split()

    yield config.get('application', 'url', fallback=DEFAULT_URL)


def get_environ(config: ConfigParser = CONFIG) -> dict:
    """Returns the environment for the subprocess."""

    env = environ.copy()
    env['DISPLAY'] = config.get('screen', 'display', fallback=DEFAULT_DISPLAY)
    return env


def main() -> int:
    """Runs the program."""

    basicConfig(format=FORMAT, level=INFO)
    load_config()
    command = tuple(get_command())
    LOGGER.info('Running: %s', command)
    completed_process = run(command, env=get_environ(), check=False)
    return completed_process.returncode
