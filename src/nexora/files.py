"""Small, explicit file helpers."""

from pathlib import Path
from typing import Union

PathLike = Union[str, Path]


def read_text(path: PathLike, *, encoding: str = "utf-8") -> str:
    """Read a text file using an explicit encoding."""
    return Path(path).read_text(encoding=encoding)


def write_text(path: PathLike, content: str, *, encoding: str = "utf-8") -> Path:
    """Write text to a file and return its path. Parent folders are not created."""
    if not isinstance(content, str):
        raise TypeError("content must be a string")
    target = Path(path)
    target.write_text(content, encoding=encoding)
    return target


def size(path: PathLike) -> int:
    """Return file size in bytes."""
    return Path(path).stat().st_size
