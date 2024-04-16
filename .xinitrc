# Source .xprofile started with startx
[ -f ~/.xprofile ] && . ~/.xprofile

# Start window manager
exec xfwm4
