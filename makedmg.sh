#! /bin/sh
test -f "Pennyworth.dmg" && rm "Pennyworth.dng"
test -d "dist/dmg" && rm -rf "dist/dmg"
# Make the dmg folder & copy our .app bundle in
mkdir -p "dist/dmg"
cp -r "dist/Pennyworth.app" "dist/dmg"
# Create the dmg.
create-dmg \
    --volname "Pennyworth" \
    --volicon "pennyworth.icns" \
    --window-pos 200 120 \
    --window-size 800 400 \
    --icon-size 100 \
    --icon "Pennyworth.app" 200 190 \
    --hide-extension "Pennyworth.app" \
    --app-drop-link 600 185 \
    "Pennyworth.dmg" \
    "dist/dmg/"