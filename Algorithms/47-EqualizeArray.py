#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    L = []
    D = {}
    length_arr = len(arr)
    for element in arr:
        if element not in D:
            count = arr.count(element)
            D[element] = count
    for key, value in D.items():
        if value > 1:
            deletion = len(arr) - value
            L.append(deletion)
        else:
            deletion = len(arr) - 1
            L.append(deletion)
    L.sort()
    print(L[0])

    return L[0]

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
