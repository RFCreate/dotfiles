#!/bin/sh

# Exit if session is wayland
if [ -n "$WAYLAND_DISPLAY" ]; then
    exit
fi

# Import environment variables into systemd user session and dbus
systemctl --user import-environment DISPLAY XAUTHORITY
dbus-update-activation-environment DISPLAY XAUTHORITY

# Set keyboard layout
setxkbmap -layout latam -variant deadtilde

# Set touchpad options
for i in $(xinput list | grep -i "touchpad" | perl -n -e'/id=(\d+)/ && print "$1\n"'); do
    xinput set-prop "$i" "libinput Accel Speed" 0.25
    xinput set-prop "$i" "libinput Natural Scrolling Enabled" 1
    xinput set-prop "$i" "libinput Tapping Enabled" 1
done

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
