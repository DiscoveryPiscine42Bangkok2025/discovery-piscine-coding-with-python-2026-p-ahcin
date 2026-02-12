#!/usr/bin/env python3

def play_with_arrays():
    arr = [2, 8, 9, 48, 8, 22, -12, 2]
    new_arr = []
   
    for x in arr:
        new_val = x + 2
        new_arr.append(new_val)
    
    print(f"Original array: {arr}")
    print(f"New array: {new_arr}")

if __name__ == "__main__":
    play_with_arrays()