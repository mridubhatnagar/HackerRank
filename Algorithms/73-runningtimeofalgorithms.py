"""
Problem Statement - https://www.hackerrank.com/challenges/runningtime/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(arr):
    count=0
    for i in range(1, len(arr)):
        value=arr[i]
        j=i-1
        while j>=0 and arr[j]>value:
            arr[j+1]=arr[j]
            arr[j]=value
            j=j-1
            count += 1
    print(count)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
