#!/bin/dash


mlalias cs2041.23T2.tutors |
sed -E -n '/Addresses/,/Owners/p' |
tail -n +2 |
head -n -1 |
tr -d ' ' |
grep -E '^z[0-9]{7}'