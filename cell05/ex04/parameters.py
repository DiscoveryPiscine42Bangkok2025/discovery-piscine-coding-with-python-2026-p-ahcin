#!/usr/bin/env python3
import sys

def count_parameters():
    all_param = len(sys.argv)
    
    num_param = all_param - 1
    
    print(f"Number of parameters: {num_param}.")

if __name__ == "__main__":
    count_parameters()