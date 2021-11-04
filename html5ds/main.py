"""Launch HTML5-based digital signage applications in a web browser."""

from logging import INFO, basicConfig
from subprocess import run

from html5ds.command import get_command, get_environ
from html5ds.config import load
from html5ds.logging import FORMAT, LOGGER


__all__ = ['main']


def main() -> int:
    """Runs the program."""

    basicConfig(format=FORMAT, level=INFO)
    load()
    command = tuple(get_command())
    LOGGER.info('Running: %s', command)
    env = get_environ()
    LOGGER.info('Environment: %s', env)
    return run(command, env=env, check=False).returncode
