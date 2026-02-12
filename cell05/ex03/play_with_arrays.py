#!/usr/bin/env python3

def play_with_arrays():
    arr = [2, 8, 9, 48, 8, 22, -12, 2]
    
    new_arr = []
    for x in arr:
        if x > 5:
            new_arr.append(x + 2)

    # set union ค่าซ้ำ
    new_set = set(new_arr)
    
    print(arr)
    print(new_set)

if __name__ == "__main__":
    play_with_arrays()