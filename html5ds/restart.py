"""Restart html5ds if it is enabled."""

from time import sleep

from html5ds import systemctl


__all__ = ['await_stop', 'restart']


TICK = 1    # seconds
UNIT = 'html5ds.service'


def await_stop() -> None:
    """Stop html5ds."""

    systemctl.stop(UNIT)

    while systemctl.is_active(UNIT):
        sleep(TICK)


def restart() -> None:
    """Restart html5ds if it is enabled."""

    if systemctl.is_enabled(UNIT):
        systemctl.start(UNIT)
