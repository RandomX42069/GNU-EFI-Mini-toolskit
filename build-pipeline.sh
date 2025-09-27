#!/bin/bash

echo "Starting pipeline..."

# Exit immediately if any command fails
set -e

# Step 1: Setup build environment
if [ -f build-setup.sh ]; then
    echo "[1/4] Running build-setup.sh..."
    bash build-setup.sh
else
    echo "Error: build-setup.sh not found!"
    exit 1
fi

# Step 2: Compile EFI application
if [ -f build-EFI-App.sh ]; then
    echo "[2/4] Running build-EFI-App.sh..."
    bash build-EFI-App.sh
else
    echo "Error: build-EFI-App.sh not found!"
    exit 1
fi

# Step 3: Prepare disk image
if [ -f build-disk.sh ]; then
    echo "[3/4] Running build-disk.sh..."
    bash build-disk.sh
else
    echo "Error: build-disk.sh not found!"
    exit 1
fi

# Step 4: Build VDI/virtual disk
if [ -f build-vdi.sh ]; then
    echo "[4/4] Running build-vdi.sh..."
    bash build-vdi.sh
else
    echo "Error: build-vdi.sh not found!"
    exit 1
fi

echo "Pipeline finished successfully!"
