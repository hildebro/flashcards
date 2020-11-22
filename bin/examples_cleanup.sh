#!/usr/bin/env bash
# Some best practice settings for bash scripts
# set -e: automatically exits on any failing command
# set -u: exits if there are any unset variables
# set -o pipefail: automatically exits, if any command in a pipe fails (normally only the last is counted)
set -euo pipefail

# Replace newline within quotes with a pipe, because the vocabulary examples are separated as such.
awk -v RS='^$' -v ORS= '{while ( match($0,/"[^"]+"/,a) ) {gsub(/\n/,"|",a[0]); print substr($0,1,RSTART-1) a[0]; $0=substr($0,RSTART+RLENGTH)} print}' $1