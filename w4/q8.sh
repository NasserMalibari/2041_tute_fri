#!/bin/dash

# ./q5.sh |
cat list |
while read zid
do 
    # echo "zid = $zid"
    ./q7.sh $zid
done |
sort |
uniq -c