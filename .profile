# Add ~/.local/bin to PATH
export PATH="${PATH}:${HOME}/.local/bin"

# Set XDG variables
export XDG_CACHE_HOME=$HOME/.cache
export XDG_CONFIG_HOME=$HOME/.config
export XDG_DATA_HOME=$HOME/.local/share
export XDG_STATE_HOME=$HOME/.local/state

# Set default editor
export EDITOR=micro

# Set python history file
export PYTHON_HISTORY="$HOME/.local/state/python/history"

# Configure git
git config --global init.defaultBranch main
git config --global alias.a   'add'
git config --global alias.aa  'add --all'
git config --global alias.au  'add --update'
git config --global alias.c   'commit'
git config --global alias.cam 'commit -am'
git config --global alias.co  'checkout'
git config --global alias.cob 'checkout -b'
git config --global alias.d   'diff'
git config --global alias.dc  'diff --cached'
git config --global alias.ds  'diff --stat'
git config --global alias.lg  'log --oneline --decorate --graph'
git config --global alias.s   'status'
