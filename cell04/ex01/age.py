#!/usr/bin/env python3

def age():
    age = int(input("Please tell me your age: "))
    print(f"You are currently {age} years old.")
    
    year = 10
    while year <= 30:
        future = age + year
        print(f"In {year} years, you'll be {future} years old.")
        year += 10

if __name__ == "__main__":
    age()