"""
MARC Converter

Converts MARC records copied from OPACs into valid MARC mnemonic format.
"""

from pathlib import Path


def load_input(filename: str) -> str:
    """Read a text file and return its contents."""
    return Path(filename).read_text(encoding="utf8")


def detect_source(text: str) -> str:
    """Determine the source format."""

    if "&#x2021;" in text:
        return "LinkCat"

    if "$a" in text:
        return "KCLS"

    return "Unknown"


def main() -> None:
    filename = "samples/input.txt"

    record = load_input(filename)
    source = detect_source(record)

    print(f"Source: {source}")
    print(f"Characters: {len(record)}")


if __name__ == "__main__":
    main()