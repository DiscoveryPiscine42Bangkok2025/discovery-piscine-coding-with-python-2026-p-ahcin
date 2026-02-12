#!/usr/bin/env python3

def to25():
    input_num = int(input("Enter a number less than 25\n"))
     
    if input_num > 25:
        print("Error")
    else:
        while input_num <= 25:
            print(f"Inside the loop, my variable is {input_num}")
            input_num += 1

if __name__ == "__main__":
    to25()