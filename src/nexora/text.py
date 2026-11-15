"""Text utilities."""

import re
import unicodedata


def clean(value: str, *, lowercase: bool = False) -> str:
    """Trim text and collapse consecutive whitespace into single spaces."""
    if not isinstance(value, str):
        raise TypeError("value must be a string")
    result = " ".join(value.split())
    return result.lower() if lowercase else result


def word_count(value: str) -> int:
    """Count words separated by whitespace or punctuation."""
    if not isinstance(value, str):
        raise TypeError("value must be a string")
    return len(re.findall(r"\b[\wÀ-ÖØ-öø-ÿ]+\b", value, flags=re.UNICODE))


def slugify(value: str, *, separator: str = "-") -> str:
    """Convert text to a simple URL/file-friendly slug."""
    if not isinstance(value, str):
        raise TypeError("value must be a string")
    if not separator or not isinstance(separator, str):
        raise ValueError("separator must be a non-empty string")
    normalized = unicodedata.normalize("NFKD", value)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    parts = re.findall(r"[a-zA-Z0-9]+", ascii_text.lower())
    return separator.join(parts)
