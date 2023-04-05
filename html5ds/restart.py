"""Restart html5ds if it is enabled."""

from html5ds import systemctl


__all__ = ['stop', 'restart']


UNIT = 'html5ds.service'


def stop() -> None:
    """Stop html5ds."""

    systemctl.stop(UNIT)


def restart() -> None:
    """Restart html5ds if it is enabled."""

    if systemctl.is_enabled(UNIT):
        systemctl.start(UNIT)
