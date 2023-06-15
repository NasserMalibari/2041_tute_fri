#!/usr/bin/sh

# if test "$#" -le 3
if [ "$#" -le 3 ]
then
    # echo "correct num of args"
    :
else
    echo "usage: give 1-3 args pls" 
    exit 0
fi

if [ "$#" -eq 1 ]
then
    last=$1
    first=1
    increment=1
fi

#TODO 2 and 3 args


# check args are integers
if [ "$last" -eq "$last" ] 2> /dev/null
then
    echo "last is a number!"
else
    echo "not a number!"
fi

exit 0

# do the print

current=$first
while [ "$current" -le "$last"  ]
do
    echo "$current"
    current=$(( current = current + 1  ))
done
