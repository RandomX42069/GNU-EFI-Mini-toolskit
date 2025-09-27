echo "GNU-EFI Mini Toolkit [Copyright 2025 RandomX]"
echo "Visit the original GNU-EFI repo for license and usage"

# Update MSYS2 package database and upgrade system
pacman -Syu --noconfirm

# Install required tools
pacman -S --noconfirm clang lld mtools dosfstools
