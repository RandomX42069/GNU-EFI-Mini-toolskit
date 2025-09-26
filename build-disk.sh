#!/bin/bash

SHELL_ARCH="x64"
SHELL="Tools/Shells/UEFI${SHELL_ARCH}Shell.efi"

COPYDIR="output"
DISKDIRNAME="Copied"
DISKNAME="disks/fat.img"
COUNT=64

# Ensure directories exist
mkdir -p disks

# Create the image
dd if=/dev/zero of=$DISKNAME bs=1M count=$COUNT

# Format as FAT32
mkfs.vfat $DISKNAME

# Create EFI folders
mmd -i $DISKNAME ::/EFI
mmd -i $DISKNAME ::/EFI/BOOT

# Copy UEFI shell
mcopy -i $DISKNAME $SHELL ::/EFI/BOOT/BOOTX64.EFI

# Create folder for extra files
mmd -i $DISKNAME ::/$DISKDIRNAME

# Copy extra files
mcopy -i $DISKNAME $COPYDIR/* ::/$DISKDIRNAME/
