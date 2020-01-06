"""
Problem Statement - https://www.hackerrank.com/challenges/pairs/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    L=[]
    arr.sort()
    print(arr)
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[j]-arr[i]==k:
                L.append([arr[i], arr[j]])

    print(L)
    result=len(L)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
