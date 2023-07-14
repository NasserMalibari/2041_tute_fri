#!/usr/bin/env python3

import sys
# from sys import foo bar
# from sys import *

n_lines = 10
if (len(sys.argv) > 1):
    num = sys.argv[1]
    # num  = -n
    if (num[0] != "-"):
        print("wrong num of args!")
    num = num[1:]
    # try:
    n_lines = int(num)
    # print(n_lines)
    # except ValueError as e:
    #     print("not an int")
curr_lines = 1
print(n_lines)
for line in sys.stdin:
    if curr_lines < n_lines:
        print(line, end = "")
        curr_lines += 1
    else:
        break
    # line.strip()
    # print(line, end="")




