#!/bin/dash

# check there is an arg

zid=$1

acc $zid |
sed -E -n '/User classes/,/Misc classes/p' |
cut -d':' -f2 |
tr ',' '\n' | tr -d ' ' |
grep -E '[A-Z]{4}[0-9]{4}t[0-3]_Student' |
cut -c'1-8'