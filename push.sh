#!/bin/env bash

# Save directory of script
scriptDir="$(dirname "$0")"

# Enable !() pattern matching
shopt -s extglob
# Includes filenames beginning with a '.' in expansion
shopt -s dotglob

# Copy all files in this repo to $HOME
cp -bur --suffix=".bak" "${scriptDir}"/!(pull.sh|push.sh|.git) "$HOME"

# Replace bookmarks path, to make it relative to user
sed -i "s|\$HOME|${HOME}|" "$HOME/.config/gtk-3.0/bookmarks"

# Add cron job for battery notifications
echo "*/1 * * * * DISPLAY=${DISPLAY:-:0} DBUS_SESSION_BUS_ADDRESS=${DBUS_SESSION_BUS_ADDRESS:-unix:path=/run/user/${UID}/bus} ${HOME}/.local/bin/battery-notify" | crontab - > /dev/null
