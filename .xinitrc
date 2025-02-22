#!/bin/sh

# Source ~/.xprofile used with startx
[ -f "$HOME/.xprofile" ] && . "$HOME/.xprofile"

# Start window manager
exec qtile start
