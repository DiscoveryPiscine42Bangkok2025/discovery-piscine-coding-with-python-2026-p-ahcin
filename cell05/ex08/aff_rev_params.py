#!/usr/bin/env python3
import sys

def reverse_params():
    if len(sys.argv) < 3:
        print("none")
        return

    curr_index = len(sys.argv) - 1
    
    while curr_index >= 1:
        print(sys.argv[curr_index])
        curr_index = curr_index - 1

if __name__ == "__main__":
    reverse_params()