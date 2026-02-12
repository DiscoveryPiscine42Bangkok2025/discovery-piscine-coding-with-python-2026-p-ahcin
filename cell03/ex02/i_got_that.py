#!/usr/bin/env python3

def i_got_that():
    ip = input("What you gotta say? : ")
    
    while ip != "STOP":
        ip = input("I got that! Anything else? : ")

if __name__ == "__main__":
    i_got_that()