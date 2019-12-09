"""
Problem Statement - https://www.hackerrank.com/challenges/insertionsort2/problem
"""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(1, len(arr)-1):
        value = arr[i]
        j=i-1
        while j>=0 and arr[j] > value:
            arr[j+1] = arr[j]
            arr[j] = value
            j=j-1
        print(*arr)
    
    value = arr[len(arr)-1]
    for i in range(len(arr)-2, -1, -1):
        if value<arr[i]:
            arr[i+1] = arr[i]
            arr[i] = value
        else:
            arr[i+1] = value
            break
    print(*arr)



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
