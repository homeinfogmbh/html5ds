"""Restart html5ds if it is enabled."""

from html5ds import systemctl


__all__ = ["restart"]


TICK = 1  # seconds
UNIT = "html5ds.service"


def restart() -> None:
    """Restart html5ds if it is enabled."""

    if systemctl.is_enabled(UNIT):
        systemctl.start(UNIT)
