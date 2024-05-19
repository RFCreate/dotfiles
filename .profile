# Add ~/.local/bin to PATH
export PATH="${PATH}:${HOME}/.local/bin"

# Export variables
export EDITOR=micro

# Change python history file
export PYTHON_HISTORY="$HOME/.local/state/python/history"

# Configure git
if [ ! -f "$HOME/.config/git/config" ]; then
    mkdir -p "$HOME/.config/git"
    touch "$HOME/.config/git/config"
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
fi
