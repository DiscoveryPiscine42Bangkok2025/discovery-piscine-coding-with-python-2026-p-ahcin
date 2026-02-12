#!/usr/bin/env python3
import sys

def upcase_it():
    if len(sys.argv) == 2:
        result = sys.argv[1].upper()
        print(result)
    else:
        print("none")

if __name__ == "__main__":
    upcase_it()