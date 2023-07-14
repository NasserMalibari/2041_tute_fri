#!/usr/bin/env python3

import sys

def head(filename, n_lines=10):
    
    with open(filename) as f:
        for (line_num, line) in enumerate(f, start = 1):
            if (line_num <= n_lines):
                print(line, end = "")



n_lines = 10
if len(sys.argv) > 1 and sys.argv[1].startswith('-'):
    n_lines = int(sys.argv.pop(1)[1:])

if len(sys.argv) == 1:
    sys.argv.append("-")

head(sys.argv[1], n_lines)
# print(sys.argv)
