"""
Problem Statement - https://www.hackerrank.com/challenges/countingsort1/problem
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
    for x in range(0, 100):
        if x not in D:
            count = arr.count(x)
            D[x] = count

    for y in range(0, 100):
        L.append(D[y])
    return L

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
