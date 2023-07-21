#!/usr/bin/python3

# alternatively
# import glob
# glob.glob(...)

from glob import glob

for filename in glob(r"*.[ch]"):
    print(filename)

# glob(...)