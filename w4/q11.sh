#!/bin/dash

if [ $# -ne 1 ]
then
    echo "usage: $0 <program name>" 1>&2
    exit 1
fi

program=$1

directories=$( echo $PATH | tr ':' ' ' )
# echo $directories
# directories = 'dir1 dir2 dir3'
for dir in $directories
do
    # see if program is in dir
    pathname=$dir/$program

    if test -x "$pathname"
    then
        ls -l "$pathname"
    fi
done