"""
Problem Statement - https://www.hackerrank.com/challenges/minimum-distances/problem

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    L=[]
    for i in range(0, len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                print(a[i], a[j])
                distance = abs(j-i)
                L.append(distance)
    if len(L) >= 1:
        minimum = min(L)
    else:
        minimum = -1
    return minimum
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    result = minimumDistances(a)
    fptr.write(str(result) + '\n')
    fptr.close()
