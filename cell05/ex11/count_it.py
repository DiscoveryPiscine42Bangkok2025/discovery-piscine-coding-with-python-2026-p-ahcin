#!/usr/bin/env python3
import sys

def count_it():
    argc = len(sys.argv) - 1
    
    if argc == 0:
        print("none")
    else:
        print(f"parameters: {argc}")

        for i in range(1, len(sys.argv)):
            arg = sys.argv[i]
            print(f"{arg}: {len(arg)}")

if __name__ == "__main__":
    count_it()