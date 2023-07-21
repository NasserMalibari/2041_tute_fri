#!/usr/bin/python3

import sys
    
# "1" -->  "    1"
# "11" --> "   11"
    
def times(rows, cols, width):

    for row in range(1, rows+1):
        print("")
        for col in range(1, cols+1):
            print(f"{row * col: >{width}}", end = "")
    print("")
if __name__ == "__main__":
    times(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))