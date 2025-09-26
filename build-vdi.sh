#!/bin/bash

# Path to the raw FAT32 image
DISK="D:/Myfiles/GNU-EFI-Toolkits/disks/fat.img"

# Path to VBoxManage
VIRTUALBOXMGR="C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe"

# Output VDI path
VDI="D:/Myfiles/GNU-EFI-Toolkits/disks/fat.vdi"

# Use PowerShell to convert raw image to VDI
powershell.exe -Command "& {& '${VIRTUALBOXMGR}' convertfromraw '${DISK}' '${VDI}' --format VDI}"

echo "Conversion complete: ${VDI}"