#!/usr/bin/env python3

def advanced_mult():
   
    table = 0
    # 0 - 10 core row
    while table <= 10:
        print(f"Table de {table}:", end="")
        
        multiplier = 0
        # 0 - 10 in each row
        while multiplier <= 10:
            result = table * multiplier
            print(f" {result}", end="")
            multiplier += 1
            
        print()
        table += 1

if __name__ == "__main__":
    advanced_mult()