#!/bin/bash
EFI_WILDCARD_SCRIPT="build-wildcard-efi.py"

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "Python not found, installing..."
    pacman -S --noconfirm python
fi

# Run the Python script
python "$EFI_WILDCARD_SCRIPT"
