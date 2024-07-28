"""
python file to get the current version read from version.txt
"""

from pathlib import Path


__all__ = ['get_version']


def get_version() -> str:
    """
    Get current library version
    """
    parent_dir = Path(__file__).parent.resolve()
    version_file = parent_dir.joinpath("version.txt")
    ver = "v"
    with open(version_file, "r", encoding='UTF-8') as f:
        ver += str(f.read().strip())
    return ver
