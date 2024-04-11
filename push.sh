#!/bin/env bash

# Save directory of script
scriptDir="$(dirname "$0")"

# Enable !() pattern matching
shopt -s extglob
# Includes filenames beginning with a '.' in expansion
shopt -s dotglob

# Copy all files in this repo to $HOME
cp -bur --suffix=".bak" "${scriptDir}"/!(pull.sh|push.sh|.git) "$HOME"
