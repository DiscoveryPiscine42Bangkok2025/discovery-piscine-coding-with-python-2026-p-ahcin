#!/usr/bin/env python3

def isneg(number):
    if number < 0:
        print("The result is negative.")
    elif number > 0:
        print("The result is positive.")
    else:
        print("The result is positive and negative.")

def mulyiply():
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))

    result = first_number * second_number
    print(f"{first_number} x {second_number} = {result}")
    isneg(result)
    

if __name__ == "__main__":
    mulyiply()