"""
Problem Statement - https://www.hackerrank.com/challenges/sherlock-and-array/problem
"""



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    print(arr)
    result=''
    for i in range(0, len(arr)):
        left_side=arr[:i]
        if left_side == []:
            left_side=[0]
        print(left_side)
        right_side=arr[i+1:]
        if right_side==[]:
            right_side=[0]
        print(right_side)

        if sum(left_side)==sum(right_side):
            result=arr[i]
            break
    print(result)    
    if result == '':
        result = "NO"
    else:
        result = "YES"
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
