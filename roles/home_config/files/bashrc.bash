# shellcheck shell=bash
compopt -o nospace ls  # Do not add space after autocompletion for 'ls' command
complete -o nospace -F _longopt source  # can't use it directly with compopt
