"""Simple systemctl bindings."""

from subprocess import CalledProcessError, CompletedProcess, run


__all__ = ['is_enabled', 'start', 'stop', 'systemctl']


def is_enabled(unit: str) -> bool:
    """Check whether the respective unit is enabled."""

    try:
        systemctl('is-enabled', unit)
    except CalledProcessError:
        return False

    return True


def start(unit: str) -> CompletedProcess:
    """Start the given unit."""

    return systemctl('start', unit)


def stop(unit: str) -> CompletedProcess:
    """Stop the given unit."""

    return systemctl('stop', unit)


def systemctl(command: str, *args: str) -> CompletedProcess:
    """Run a systemctl command."""

    return run(['systemctl', command, *args], check=True)
