from pathlib import Path


def make_empty(path: Path) -> Path:
    """Create an empty file at the given path."""
    assert not path.is_file(), "File already exists"
    with open(path, "w") as f:
        f.write("")
    return path
