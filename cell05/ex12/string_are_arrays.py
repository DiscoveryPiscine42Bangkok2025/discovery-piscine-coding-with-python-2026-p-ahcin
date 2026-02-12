#!/usr/bin/env python3
import sys

def find_z():
    if len(sys.argv) != 2:
        print("none")
        return

    ip_string = sys.argv[1]
    result = ""
    
    for char in ip_string:
        if char == 'z':
            result += "z"

    if result == "":
        print("none")
    else:
        print(result)

if __name__ == "__main__":
    find_z()