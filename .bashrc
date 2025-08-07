# History file configuration options
HISTCONTROL="erasedups:ignorespace"
HISTFILE="$HOME/.local/state/bash/history"
HISTFILESIZE=10000
HISTSIZE=10000

# Set window title to last command
PS0='\[\e]2;$(history 1 | sed "s/^\\s*[0-9]*\\s*//g")\a\]'
# Do not reset the title after command finish
PROMPT_COMMAND=''
# Set primary prompt style
PS1="\[$(tput bold)\]\[$(tput setaf 1)\][\[$(tput setaf 3)\]\t \[$(tput setaf 5)\]\w\[$(tput setaf 1)\]]\[$(tput setaf 7)\]\\$ \[$(tput sgr0)\]"

# Check for script and source it
source_script() {
    [ -f "$1" ] && source "$1"
}

# Load aliases
source_script "$HOME/.config/aliasrc"

# dotfiles alias completion
source_script /usr/share/bash-completion/completions/git && __git_complete dotfiles __git_main

# Load fzf CTRL-R history search
export FZF_DEFAULT_OPTS="--height 100% --layout=default --border"
FZF_CTRL_T_COMMAND="" FZF_ALT_C_COMMAND="" source_script /usr/share/fzf/key-bindings.bash

shopt -s autocd         # Change directory automatically
shopt -s dotglob        # Match all files including dotfiles
shopt -s histappend     # Append to history even when session history exceeds HISTSIZE

bind 'set completion-ignore-case on'    # Insensitive completion
bind 'set bell-style none'              # Remove beep

# Remove source function
unset -f source_script
