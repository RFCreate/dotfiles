# History file configuration options
HISTFILE="$HOME/.local/state/zsh/history"
HISTSIZE=10000
SAVEHIST=10000

# Set window title to last command
function preexec () {
    builtin print -n -- "\e]2;$1\a"
}

# Change word delimeter to alphanumerics only
autoload -U select-word-style
select-word-style bash

# Load completion module
autoload -Uz compinit
zmodload -i zsh/complist
[ -d "$HOME/.cache/zsh" ] || mkdir -p "$HOME/.cache/zsh"
compinit -d "$HOME/.cache/zsh/zcompdump-$ZSH_VERSION"

# Check for script and source it
source_script() {
    [ -f "$1" ] && source "$1"
}

# Load aliases
source_script "$HOME/.config/aliasrc"
# Load env variables
source_script "$HOME/.config/envrc"

# Load zsh plugins
source_script /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source_script /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source_script /usr/share/zsh/plugins/zsh-history-substring-search/zsh-history-substring-search.zsh

# Load custom prompt
eval "$(starship init zsh)"

# Load fzf CTRL-R history search
export FZF_DEFAULT_OPTS="--height 100% --layout=default --border"
FZF_CTRL_T_COMMAND="" FZF_ALT_C_COMMAND="" source_script /usr/share/fzf/key-bindings.zsh

# Set emacs keybindings
bindkey -e
# Load terminfo database
zmodload -i zsh/terminfo

# Check that key exists and bind it
bindterminfo() {
    [ -n "${terminfo[$1]}" ] && bindkey "${terminfo[$1]}" "$2"
}

bindkey '^[[7~' beginning-of-line                   # Home key
bindkey '^[[H' beginning-of-line                    # Home key
bindterminfo khome beginning-of-line                # Home key
bindkey '^[[8~' end-of-line                         # End key
bindkey '^[[F' end-of-line                          # End key
bindterminfo kend end-of-line                       # End key
bindkey '^[[2~' overwrite-mode                      # Insert key
bindterminfo kich1 overwrite-mode                   # Insert key
bindkey '^[[3~' delete-char                         # Delete key
bindterminfo kdch1 delete-char                      # Delete key
bindkey '^[[3;5~' kill-word                         # Ctrl + Delete
bindkey '^H' backward-kill-word                     # Ctrl + Backspace
bindkey '^[[1;5D' backward-word                     # Ctrl + Left arrow
bindkey '^[[1;5C' forward-word                      # Ctrl + Right arrow
bindkey '^Z' undo                                   # Ctrl + z
bindkey '^[[Z' reverse-menu-complete                # Shift + Tab
bindkey '^[' kill-whole-line                        # Esc key
bindkey '^[[A' history-substring-search-up          # Up arrow
bindterminfo kcuu1 history-substring-search-up      # Up arrow
bindkey '^[[B' history-substring-search-down        # Down arrow
bindterminfo kcud1 history-substring-search-down    # Down arrow
bindkey '^[[5~' history-beginning-search-backward   # Page up key
bindterminfo kpp history-beginning-search-backward  # Page up key
bindkey '^[[6~' history-beginning-search-forward    # Page down key
bindterminfo knp history-beginning-search-forward   # Page down key

# Shorter cd command
export DIRSTACKSIZE=10
alias 0='dirs -v'
alias 1='cd -1'
alias 2='cd -2'
alias 3='cd -3'
alias 4='cd -4'
alias 5='cd -5'
alias 6='cd -6'
alias 7='cd -7'
alias 8='cd -8'
alias 9='cd -9'

setopt autocd               # Change directory automatically
setopt autopushd            # Push old directory to the stack
setopt pushdignoredups      # Ignore duplicates in the stack
setopt pushdminus           # Use -n to specify a directory in the stack
setopt alwaystoend          # Move cursor to the end after completion
setopt globdots             # Match all files including dotfiles
setopt extendedhistory      # Save command with timestamp
setopt histexpiredupsfirst  # Remove duplicates from history file when full
setopt histfindnodups       # Do not show duplicates in history search
setopt histignorealldups    # Remove duplicates of newer command from history list
setopt histignoredups       # Do not save duplicates of previous commands to history list
setopt histignorespace      # Do not save leading spaces to history
setopt histsavenodups       # Do not save duplicates to history file
setopt histverify           # Do not execute history expansion
setopt incappendhistorytime # Save command to history after execution with timestamp
setopt interactivecomments  # Allow comments
unsetopt beep               # Disable error beep

zstyle ':completion:*' menu select                                                  # Highlight selection in menu complete
zstyle ':completion:*' accept-exact '*(N)'                                          # Accept only match without double tab
zstyle ':completion:*' use-cache true                                               # Use completion cache
zstyle ':completion:*' cache-path "$HOME/.cache/zsh/zcompcache"                     # Set path of dumped completion data
zstyle ':completion:*' matcher-list 'm:{[:lower:][:upper:]}={[:upper:][:lower:]}'   # Make matches case-insensitive
zstyle ':completion:*' rehash true                                                  # Reload new executables in path
zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"                             # Use same ls colors for completion

# Remove source function
unset -f source_script bindterminfo
