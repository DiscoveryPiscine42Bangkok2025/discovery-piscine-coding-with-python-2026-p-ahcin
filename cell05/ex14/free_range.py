#!/usr/bin/env python3
import sys

def free_range():
    if len(sys.argv) != 3:
        print("none")
        return

    start = int(sys.argv[1])
    end = int(sys.argv[2])
    result = list(range(start, end + 1))

    print(result)

if __name__ == "__main__":
    free_range()