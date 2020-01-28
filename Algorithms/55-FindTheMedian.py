"""
Problem Statement - https://www.hackerrank.com/challenges/find-the-median/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findMedian function below.
def findMedian(arr):
    arr.sort()
    print(arr)
    n = len(arr) - 1
    if n%2!=0:
        median = int((n+1)/2)
    else:
        median = int((n/2 + (n/2 + 1))/2)
    result = arr[median]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
