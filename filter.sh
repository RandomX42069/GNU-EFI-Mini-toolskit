#!/bin/bash
FILTER_SCRIPT="filter.py"

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "Python not found, installing..."
    pacman -S --noconfirm python
fi

python ${FILTER_SCRIPT}