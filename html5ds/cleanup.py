"""Cleanup of browser data."""

from logging import basicConfig, getLogger
from pathlib import Path
from shutil import rmtree
from typing import Iterator

from html5ds.logging import FORMAT


__all__ = ['cleanup_chromium_cache', 'cleanup_chromium_crash_logs']


LOGGER = getLogger(__file__)


def cleanup_chromium_cache() -> None:
    """Clean up chromium crash logs."""

    basicConfig(format=FORMAT)

    for profile in chromium_profiles():
        if (cache := profile.joinpath('Cache')).is_dir():
            if (cache_data := cache.joinpath('Cache_Data')).is_dir():
                for file in cache_data.iterdir():
                    if file.is_file():
                        file.unlink()
                        LOGGER.info('Removed file: %s', file)
                    elif file.is_dir():
                        rmtree(file)
                        LOGGER.info('Removed directory: %s', file)


def cleanup_chromium_crash_logs() -> None:
    """Remove chromium crash log files."""

    basicConfig(format=FORMAT)

    for dir_name in ['attachments', 'completed', 'new', 'pending']:
        if (path := chromium_crash_reports_dir().joinpath(dir_name)).is_dir():
            for file in path.iterdir():
                file.unlink()
                LOGGER.info('Removed file: %s', file)


def chromium_cache_dir() -> Path:
    """Return the current user's chromium cache dir."""

    return Path.home() / '.cache' / 'chromium'


def chromium_config_dir() -> Path:
    """Return the current user's chromium config dir."""

    return Path.home() / '.config' / 'chromium'


def chromium_crash_reports_dir() -> Path:
    """Return the current user's chromium crash reports dir."""

    return chromium_config_dir() / 'Crash Reports'


def chromium_profiles() -> Iterator[Path]:
    """Yield chromium profile directories."""

    for path in chromium_cache_dir().iterdir():
        if path.is_dir():
            yield path
