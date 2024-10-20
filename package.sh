#!/bin/sh
# Create folders.
[ -e package ] && rm -r package
mkdir -p package/opt
mkdir -p package/usr/share/applications
mkdir -p package/usr/share/icons/hicolor/scalable/apps

# Copy files (change icon names, add lines for non-scaled icons)
cp -r dist/Pennyworth package/opt/pennyworth
cp pennyworth.ico package/usr/share/icons/hicolor/scalable/apps/pennyworth.ico
cp pennyworth.desktop package/usr/share/applications

# Change permissions
find package/opt/pennyworth -type f -exec chmod 644 -- {} +
find package/opt/pennyworth -type d -exec chmod 755 -- {} +
find package/usr/share -type f -exec chmod 644 -- {} +
chmod +x package/opt/pennyworth/Pennyworth
