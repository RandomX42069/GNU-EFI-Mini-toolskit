import subprocess
import os
from pathlib import Path

ARCH="x86_64"
TOOL_PATH_CONFIG="GNU-EFI-Toolkits"
INCLUDES=f"-I./{TOOL_PATH_CONFIG}/gnu-inc -I./{TOOL_PATH_CONFIG}/gnu-inc/{ARCH}"
TARGET="-target x86_64-pc-windows-msvc"
CFLAGS=f"{INCLUDES} {TARGET} -O2 -ffreestanding -fshort-wchar -fno-exceptions -fno-stack-protector -fno-builtin -nostdlib -Wall "

def wildCard_CLANG(startDir: str):
    for dirpath, dirnames, filenames in os.walk(os.path.abspath(startDir)):
        for d in dirnames:
            print(os.path.join(dirpath, d))

        for f in filenames:
            path = Path(os.path.join(dirpath, f))
            print(path)

            if path.suffix == ".c":
                print(f"compiling: {path}")
                subprocess.call([CFLAGS, f"-c {path} -o {path.name}.o"])
            else:
                print(f"skipped: {path}")
