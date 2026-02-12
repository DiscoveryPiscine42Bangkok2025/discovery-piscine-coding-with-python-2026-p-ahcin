#!/usr/bin/env python3
import sys

def append_ism():
    if len(sys.argv) == 1:
        print("none")
        return
    
    for i in range(1, len(sys.argv)):
        word = sys.argv[i]
      
        if not word.endswith("ism"):
            print(word + "ism")

if __name__ == "__main__":
    append_ism()