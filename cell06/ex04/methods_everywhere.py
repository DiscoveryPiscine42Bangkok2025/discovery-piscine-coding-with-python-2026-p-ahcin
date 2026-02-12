#!/usr/bin/env python3
import sys

# more than 8 
# get 1st 8 char
def shrink(s):
    res = ""
    i = 0
    while i < 8:
        res += s[i]
        i += 1
    print(res)

# shorter than 8
# append 'Z' until len == 8
def enlarge(s):
    res = s
    while len(res) < 8:
        res += 'Z'
    print(res)

def main():
    if len(sys.argv) < 2:
        print("none")
        return

    for i in range(1, len(sys.argv)):
        arg = sys.argv[i]
        length = len(arg)
            
        if length > 8:
            shrink(arg)
        elif length < 8:
            enlarge(arg)
        else:
            print(arg)

if __name__ == "__main__":
    main()