import subprocess
import os
from pathlib import Path
import sys

# Linker executable and base flags
LFLAGS = ["lld-link", "/subsystem:efi_application", "/entry:efi_main"]

# Get directory argument
if len(sys.argv) < 2:
    print("Usage: python build-lld.py <directory>")
    sys.exit(1)

DIR = Path(sys.argv[1])

def wildCard_lldLINK(startDir: Path):
    # Collect all .o files first
    o_files = list(startDir.rglob("*.o"))
    if not o_files:
        print("No object files found!")
        return

    # Link each .o file individually to an .efi
    for o_file in o_files:
        out_file = o_file.with_suffix(".efi")
        print(f"linking: {o_file} -> {out_file}")
        subprocess.run(LFLAGS + [str(o_file), "/out:" + str(out_file)], check=True)

wildCard_lldLINK(DIR)