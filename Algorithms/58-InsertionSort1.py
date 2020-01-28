"""
Problem Statement - https://www.hackerrank.com/challenges/insertionsort1/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    temp = arr[n-1]
    result = []
    for i in range(n-2, -1, -1):
        if arr[i] > temp:
            arr[i+1] = arr[i]
        elif arr[i] < temp:
            arr[i+1] = temp
            break
        print(*arr)
    if temp < arr[0]:
        arr[0]=temp
    print(*arr)
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)
