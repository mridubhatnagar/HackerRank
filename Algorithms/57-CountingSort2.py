"""
Problem Statement - https://www.hackerrank.com/challenges/countingsort2/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    D = {}
    L = []
    L1 = []
    for x in range(0, 100):
        if x not in D:
            count = arr.count(x)
            D[x] = count

    for y in range(0, 100):
        L.append(D[y])

    for i in range(0, 100):
        for j in range(0, L[i]):
            L1.append(i)
    
    return L1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
