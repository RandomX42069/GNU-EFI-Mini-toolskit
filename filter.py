import os
import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: python filter.py <directory>")
    sys.exit(1)

DIR = sys.argv[1]

def filterOut(startDir: str, extensions: list[str]):
    for dirpath, dirnames, filenames in os.walk(os.path.abspath(startDir)):
        for f in filenames:
            path = Path(dirpath) / f
            if path.suffix.lower() in extensions:  # match case-insensitive
                print(f"Skipped: {path}")
            else:
                try:
                    os.remove(path)
                    print(f"Removed: {path}")
                except Exception as e:
                    print(f"Failed to remove {path}: {e}")

def filterEFI():
    filterOut(DIR, [".efi"])

if __name__ == "__main__":
    filterEFI()
