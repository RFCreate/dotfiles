#!/usr/bin/env bash

# Terminate polybar
# killall -q polybar
# Terminate polybar if ipc is enabled
polybar-msg cmd quit

# Give time for polybar to exit
sleep 1

# Reload qtile config
qtile cmd-obj -o cmd -f reload_config

# Launch polybar
polybar main 2>&1 | tee -a /tmp/polybar.log & disown
