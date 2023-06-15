#!/bin/sh


while read id mark
do
    # ... insert mark/grade checking here ...
    echo -n "$id "

    # check its an integer


    # print the mark out
    if [ $mark -ge 85 ]
    then
        echo "HD"
    fi

done # < student