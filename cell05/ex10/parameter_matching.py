#!/usr/bin/env python3
import sys

def match_parameter():
    if len(sys.argv) != 2:
        print("none")
        return

    argv1 = sys.argv[1]
    ip = input("What was the parameter? ")

    if ip == argv1:
        print("Good job!")
    else:
        print("Nope, sorry...")

if __name__ == "__main__":
    match_parameter()