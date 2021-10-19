"""Configuration file parsing and loading."""

from configparser import ConfigParser
from pathlib import Path


__all__ = ['CONFIG', 'CONFIG_FILE', 'load']


CONFIG = ConfigParser()
CONFIG_FILE = Path('/etc/html5ds.conf')


def load(file: Path = CONFIG_FILE) -> list[str]:
    """Loads the config file."""

    return CONFIG.read(file)
