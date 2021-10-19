"""Common types."""

from typing import NamedTuple


__all__ = ['Position', 'Resolution']


class Position(NamedTuple):
    """Represents a screen position."""

    x: int
    y: int


class Resolution(NamedTuple):
    """Represents a screen resolution."""

    width: int
    height: int
