#!/usr/bin/env python3

def table():
    num = int(input("Enter a number\n"))
    
    i = 0
    while i < 10:
        result = i * num
        print(f"{i} x {num} = {result}")
        i += 1
        
if __name__ == "__main__":
    table()