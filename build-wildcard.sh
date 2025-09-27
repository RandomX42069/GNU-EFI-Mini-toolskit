#!/bin/bash
WILDCARD_SCRIPT="build-wildcard.py"

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "Python not found, installing..."
    pacman -S --noconfirm python
fi

# Run the Python script
python "$WILDCARD_SCRIPT"
