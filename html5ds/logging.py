"""Logging facility."""

from logging import getLogger


__all__ = ['FORMAT', 'LOGGER']


FORMAT = '[%(levelname)s] %(name)s: %(message)s'
LOGGER = getLogger('html5ds')
