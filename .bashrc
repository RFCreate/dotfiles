# Set prompt style
export PS1="\[$(tput bold)\]\[$(tput setaf 1)\][\[$(tput setaf 3)\]\t \[$(tput setaf 5)\]\w\[$(tput setaf 1)\]]\[$(tput setaf 7)\]\\$ \[$(tput sgr0)\]"

# History file configuration options
export HISTCONTROL="erasedups:ignorespace"
export HISTFILE="$HOME/.local/state/bash/history"
export HISTFILESIZE=10000
export HISTSIZE=10000

# Check for script and source it
source_script() {
    [ -f "$1" ] && source "$1"
}

# Load aliases
source_script "$HOME/.config/aliasrc"

# Alias completion for dotfiles
source_script /usr/share/bash-completion/completions/git && __git_complete dotfiles __git_main

# Load fzf CTRL-R history search
export FZF_DEFAULT_OPTS="--height 100% --layout=default --border"
FZF_CTRL_T_COMMAND="" FZF_ALT_C_COMMAND="" source_script /usr/share/fzf/key-bindings.bash

# Remove source function
unset -f source_script
