#!/bin/sh

# Save directory of script
scriptDir="$(dirname "$0")"

# Get mousepad settings
dconf dump /org/xfce/mousepad/preferences/ > "$HOME/.config/Mousepad/dconf"

# Copy all files from $HOME to this repo
# shellcheck disable=SC2016
find "$scriptDir" -type f -not -path "./.git/*" -not -path ./pull.sh -not -path ./push.sh \
    -exec test -f "$HOME"/{} \; -exec sh -c 'cmp -s "$HOME/$1" "$1" || cp -u "$HOME/$1" "$1"' sh '{}' \;

# Replace bookmarks path, to make it relative to user
sed -i "s|${HOME}|\$HOME|" "$scriptDir/.config/gtk-3.0/bookmarks"
