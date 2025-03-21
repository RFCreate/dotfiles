# Add ~/.local/bin to PATH
export PATH="${PATH}:${HOME}/.local/bin"

# Set XDG variables
export XDG_CACHE_HOME="$HOME/.cache"
export XDG_CONFIG_HOME="$HOME/.config"
export XDG_DATA_HOME="$HOME/.local/share"
export XDG_STATE_HOME="$HOME/.local/state"

# Set default editor
export EDITOR="micro"

# Set history file of applications
export PYTHON_HISTORY="$XDG_STATE_HOME/python/history"
export MYSQL_HISTFILE="$XDG_STATE_HOME/mysql/history"
# Set config directory of applications
export DOCKER_CONFIG="$XDG_CONFIG_HOME/docker"

# Set pager for bat command (no -F --quit-if-one-screen)
export BAT_PAGER="less -R"
# Set pager for systemd commands (no -S --chop-long-lines)
export SYSTEMD_LESS="FRXMK"
# Set pager for man command (syntax highlighting)
export MANPAGER="sh -c 'sed -u -e \"s/\\x1B\[[0-9;]*m//g; s/.\\x08//g\" | bat -p -lman'"
