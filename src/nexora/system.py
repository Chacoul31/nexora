"""Cross-platform system information."""

import os
import platform
import sys
from typing import Dict, Any


def platform_name() -> str:
    """Return a normalized platform name: windows, linux, macos or other."""
    name = sys.platform
    if name.startswith("win"):
        return "windows"
    if name.startswith("linux"):
        return "linux"
    if name == "darwin":
        return "macos"
    return "other"


def info() -> Dict[str, Any]:
    """Return basic system information without collecting sensitive data."""
    return {
        "platform": platform_name(),
        "system": platform.system(),
        "release": platform.release(),
        "machine": platform.machine(),
        "python": platform.python_version(),
        "cpu_count": os.cpu_count(),
    }
