import os
import sys
from pathlib import Path
import shutil

if len(sys.argv) < 2:
    print("Usage: python split_files.py <directory>")
    sys.exit(1)

BASE_DIR = Path(sys.argv[1]).resolve()

# Mapping extensions → destination folder
DEST_MAP = {
    ".c": "c_sources",
    ".o": "objects",
    ".obj": "objects",
    ".efi": "efi_bins",
}

def split_files(base_dir: Path, dest_map: dict[str, str]):
    for dirpath, dirnames, filenames in os.walk(base_dir):
        for f in filenames:
            src_path = Path(dirpath) / f
            ext = src_path.suffix.lower()

            if ext in dest_map:
                # destination root for this extension
                dest_root = base_dir / dest_map[ext]

                # keep relative subfolder structure
                rel_path = src_path.relative_to(base_dir)
                dest_path = dest_root / rel_path

                dest_path.parent.mkdir(parents=True, exist_ok=True)

                try:
                    shutil.copy2(src_path, dest_path)  # copy file (with metadata)
                    print(f"Copied: {src_path} → {dest_path}")
                except Exception as e:
                    print(f"Failed to copy {src_path}: {e}")

if __name__ == "__main__":
    split_files(BASE_DIR, DEST_MAP)