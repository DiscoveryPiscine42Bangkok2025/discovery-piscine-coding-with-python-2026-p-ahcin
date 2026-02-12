#!/usr/bin/env python3
import sys

def downcase_it(s):
    return s.lower()

def main():
    if len(sys.argv) == 1:
        print("none")
        return

    for i in range(1, len(sys.argv)):
        result = downcase_it(sys.argv[i])
        print(result)

if __name__ == "__main__":
    main()