#!/bin/sh

# Exit if session is wayland
if [ -n "$WAYLAND_DISPLAY" ]; then
    exit
fi

# Source ~/.xprofile in case it was missed
[ -f "$HOME/.xprofile" ] && . "$HOME/.xprofile"

# Import environment variables into systemd user session and dbus
systemctl --user import-environment DISPLAY XAUTHORITY
dbus-update-activation-environment DISPLAY XAUTHORITY

# Start screenlocker and lock after 5 minutes
xset s on && xset s 300
xss-lock --transfer-sleep-lock -- i3lock -c 333333 --nofork &

# Start polkit agent
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# Start notification daemon
dunst &

# Start clipboard manager
greenclip daemon &

# Start colour temperature adjustment
redshift &

# Start network manager tray icon
nm-applet &

# Start battery notifier
battery-notify &

# Activate numlock
numlockx &
