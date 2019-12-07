"""
Problem Statement - https://www.hackerrank.com/challenges/beautiful-triplets/problem
"""



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    L=[]
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                print(i,j,k)
                if (arr[j] - arr[i]==d) and (arr[k] - arr[j]==d):
                    L.append((arr[i],arr[j],arr[k]))
    print(L)
    result = len(L)
    return result 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
