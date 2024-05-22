# Print help message if tmp file and script exist
if [ ! -f /tmp/zplugins ] && [ -f "$ZDOTDIR/zplugins.sh" ]; then
    printf "Install/Update zsh plugins with 'source \$ZDOTDIR/zplugins.sh'\n\n"
    touch /tmp/zplugins
fi

# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
    source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# History file configuration options
export HISTFILE="$HOME/.local/state/zsh/history"
export HISTSIZE=10000
export SAVEHIST=10000

# Change word delimeter to alphanumerics only
autoload -U select-word-style
select-word-style bash

# Add zsh-completions to fpath
[ -d "$ZDOTDIR/zsh-completions/src" ] && fpath=("$ZDOTDIR/zsh-completions/src" $fpath)

# Load completion module
autoload -Uz compinit
zmodload -i zsh/complist
compinit -d "$HOME/.cache/zsh/zcompdump-$ZSH_VERSION"

# Check for script and source it
source_script() {
    [ -f "$1" ] && source "$1"
}

# Load aliases
source_script "$HOME/.config/aliasrc"

# Source config files
source_script "$ZDOTDIR/.setopt"
source_script "$ZDOTDIR/.zstyle"
source_script "$ZDOTDIR/.bindkey"

# Load zsh plugins
source_script "$ZDOTDIR/zsh-autosuggestions/zsh-autosuggestions.zsh"
source_script "$ZDOTDIR/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh"
source_script "$ZDOTDIR/zsh-history-substring-search/zsh-history-substring-search.zsh"
source_script "$ZDOTDIR/powerlevel10k/powerlevel10k.zsh-theme"

# Source powerlevel10k config file
source_script "$ZDOTDIR/.p10k.zsh"

# Load fzf CTRL-R history search
export FZF_DEFAULT_OPTS="--height 100% --layout=default --border"
FZF_CTRL_T_COMMAND="" FZF_ALT_C_COMMAND="" source_script /usr/share/fzf/key-bindings.zsh

# Remove source function
unset -f source_script
