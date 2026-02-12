#!/usr/bin/env python3
import sys

def downcase_it():
   
    if len(sys.argv) == 2:
        result = sys.argv[1].lower()
        print(result)
    else:
        print("none")

if __name__ == "__main__":
    downcase_it()