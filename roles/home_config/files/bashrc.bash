# shellcheck shell=bash
# Do not add space after autocompletion for following commands
compopt -o nospace ls
complete -o nospace -F _longopt source # can't use it directly with compopt
