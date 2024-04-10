# Remove file with Xorg variables
[ -n "$DISPLAY" ] && [ -f "$HOME/.Xenv" ] && rm "$HOME/.Xenv"
