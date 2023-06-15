#!/usr/bin/sh

for file in *.c # --> for file in a.c b.c wc.c ....
do
    echo "$file includes:"

    grep -E '^#include' "$file" |
    sed -E -e 's/[>"][^>"<]*$//' |  # remove end whitespace and <
    sed -E 's/^#include([[:space:]])*[<"]/    /' # remove starting bit from line

    # sed -e 'script1' -e 'script2'

done