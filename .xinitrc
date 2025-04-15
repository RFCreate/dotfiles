#!/bin/sh

# Source ~/.xprofile when using startx
[ -f "$HOME/.xprofile" ] && . "$HOME/.xprofile"

# Start window manager
exec qtile start
