"""Restart html5ds if it is enabled."""

from html5ds import systemctl


__all__ = ['main']


UNIT = 'html5ds.service'


def main() -> None:
    """Restart html5ds if it is enabled."""

    if systemctl.is_enabled(UNIT):
        systemctl.start(UNIT)
