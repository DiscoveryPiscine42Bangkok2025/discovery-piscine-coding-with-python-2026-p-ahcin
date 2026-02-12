#!/usr/bin/env python3

def password():
    password = "Python is awesome"
    input_password = input()

    if input_password == password:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")

if __name__ == "__main__":
    password()