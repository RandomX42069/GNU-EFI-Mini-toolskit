#!/bin/bash
SPLIT_SCRIPT="split.py"

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "Python not found, installing..."
    pacman -S --noconfirm python
fi

python ${SPLIT_SCRIPT}