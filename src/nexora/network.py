"""Basic network checks."""

import socket


def is_online(*, host: str = "1.1.1.1", port: int = 53, timeout: float = 2.0) -> bool:
    """Check whether a TCP connection can be established to host:port.

    This is a connectivity probe, not a guarantee that every website is reachable.
    """
    if timeout <= 0:
        raise ValueError("timeout must be greater than zero")
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (OSError, socket.timeout):
        return False
