#!/usr/bin/python3

import sys

def main():
    words1 = set()
    words2 = set()  

    with open(sys.argv[1]) as f1:
        for word in f1:
            word = word.strip()
            words1.add(word)
    
    with open(sys.argv[2]) as f2:
        for word in f2:
            word = word.strip()
            words2.add(word)
    

    for word in sorted(words1 - words2):
        print(word)
            
    

if __name__ == "__main__":
    main()