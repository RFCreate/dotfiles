# Add ~/.local/bin to PATH
export PATH="${PATH}:${HOME}/.local/bin"

# Set XDG variables
export XDG_CACHE_HOME="$HOME/.cache"
export XDG_CONFIG_HOME="$HOME/.config"
export XDG_DATA_HOME="$HOME/.local/share"
export XDG_STATE_HOME="$HOME/.local/state"

# Set default editor
export EDITOR=micro

# Set history file of applications
export PYTHON_HISTORY="$XDG_STATE_HOME/python/history"
export MYSQL_HISTFILE="$XDG_STATE_HOME/mysql/history"
# Set config directory of applications
export DOCKER_CONFIG="$XDG_CONFIG_HOME"/docker

# Set bat as pager for man command
export MANPAGER="sh -c 'col -bx | bat -l man -p'"
export MANROFFOPT="-c"

# Do not wrap lines in systemd commands
export SYSTEMD_LESS=FRXMK

# Set bat to always use pager
export BAT_PAGER="less -R"
