#!/usr/bin/env python3
import sys

def first_param():
    if len(sys.argv) <= 1:
        print("none")
    else:
        print(sys.argv[1])

if __name__ == "__main__":
    first_param()