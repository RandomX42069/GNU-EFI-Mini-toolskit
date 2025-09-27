import subprocess
import os
from pathlib import Path

# Configuration
ARCH = "x86_64"
TOOL_PATH = Path.cwd()  # Use current OS working directory
INCLUDES = f"-I{TOOL_PATH}/gnu-inc -I{TOOL_PATH}/gnu-inc/{ARCH} -I{TOOL_PATH}/edk2-inc"
TARGET = "-target x86_64-pc-windows-msvc"
CFLAGS = f"{INCLUDES} {TARGET} -O2 -ffreestanding -fshort-wchar -fno-exceptions -fno-stack-protector -fno-builtin -nostdlib -Wall"

CLANG_CMD = "clang"  # Change to full path if needed, e.g., D:/Myfiles/PyQt6 Editor/bin/clang.exe

def wildCard_CLANG(startDir: str):
    startDir = Path(startDir).resolve()
    for dirpath, dirnames, filenames in os.walk(startDir):
        for d in dirnames:
            print(Path(dirpath) / d)

        for f in filenames:
            path = Path(dirpath) / f
            print(path)

            if path.suffix == ".c":
                out_file = path.with_suffix(".o")
                print(f"Compiling: {path} -> {out_file}")

                # Build the command
                cmd = [
                    CLANG_CMD,
                    *CFLAGS.split(),
                    "-c",
                    str(path),
                    "-o",
                    str(out_file)
                ]

                # Execute the compiler
                subprocess.run(cmd, check=True)
            else:
                print(f"Skipped: {path}")

# Example usage
# wildCard_CLANG("src")
