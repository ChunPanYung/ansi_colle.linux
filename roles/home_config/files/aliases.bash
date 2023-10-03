# shellcheck shell=bash
alias less='less --raw-control-chars'
# Docker Container
alias aws='docker run --rm -ti -v ~/.aws:/root/.aws -v $(pwd):/aws amazon/aws-cli'
