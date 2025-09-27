#!/bin/bash

ARCH="x86_64"
FILE="example.c"
OBJDIR="output"
OUTPUT="$OBJDIR/compiled.o"
EFI_OUTPUT="$OBJDIR/compiled.efi"

mkdir -p "$OBJDIR"

# target triple for x86_64 UEFI
TARGET="-target x86_64-pc-windows-msvc"

INCLUDES="-I./gnu-inc -I./gnu-inc/$ARCH"

CFLAGS="$TARGET $INCLUDES -O2 -ffreestanding -fshort-wchar -fno-exceptions -fno-stack-protector -fno-builtin -nostdlib -Wall"

# Compile to .obj
clang $CFLAGS -c "$FILE" -o "$OUTPUT"

# Link using lld-link (MSVC style)
lld-link \
    /subsystem:efi_application \
    /entry:efi_main \
    /out:"$EFI_OUTPUT" \
    "$OUTPUT" \
    build/*.o
