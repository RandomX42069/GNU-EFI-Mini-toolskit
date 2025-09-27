import subprocess
import os
from pathlib import Path
import sys

ARCH = "x86_64"
INCLUDES = [f"-I./gnu-inc", f"-I./gnu-inc/{ARCH}", f"-I./edk2-inc", f"-I./custom-inc"] # since some components are coming from edk2 so 
TARGET = ["-target", "x86_64-pc-windows-msvc"]                                                            # I guess I'll make a full kit in the future
CFLAGS = ["clang", *INCLUDES, *TARGET,
          "-O2", "-ffreestanding", "-fshort-wchar",
          "-fno-exceptions", "-fno-stack-protector",
          "-fno-builtin", "-nostdlib", "-Wall"]

# Get directory argument
if len(sys.argv) < 2:
    print("Usage: python build-wildcard.py <directory>")
    sys.exit(1)

DIR = sys.argv[1]

def wildCard_CLANG(startDir: str):
    for dirpath, _, filenames in os.walk(os.path.abspath(startDir)):
        for f in filenames:
            path = Path(dirpath) / f
            if path.suffix == ".c":
                out_file = path.with_suffix(".o")
                print(f"compiling: {path} -> {out_file}")
                subprocess.run(CFLAGS + ["-c", str(path), "-o", str(out_file)], check=True)
            else:
                print(f"skipped: {path}")

wildCard_CLANG(DIR)
