#!/usr/bin/env python3

import math

def round_up():
    num = float(input("Give me a number: "))
    result = math.ceil(num)

    print(result)

if __name__ == "__main__":
    round_up()