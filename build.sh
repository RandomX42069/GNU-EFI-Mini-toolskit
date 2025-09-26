FILE="example.c"
OBJDIR="output"
OUTPUT="$OBJDIR/compiled.o"
EFI_OUTPUT="$OBJDIR/compiled.efi"
mkdir -p "$OBJDIR"

# target triple for x86_64 PE/COFF
TARGET="-target x86_64-pc-windows-msvc"

INCLUDES="-I./includes -I./gnu/inc"
CFLAGS="$TARGET $INCLUDES -O2 -ffreestanding -fshort-wchar -fno-exceptions -fno-stack-protector -fno-builtin -nostdlib -mno-red-zone -Wall"

clang $CFLAGS -c "$FILE" -o "$OUTPUT"

# Link with ld.lld producing a PE/COFF image with subsystem EFI application
ld.lld -flavor gnu \
       --image-base=0x400000 \
       --subsystem=efi_application \
       --entry=efi_main \
       -o "$EFI_OUTPUT" \
       "$OUTPUT" \
       build/*.o