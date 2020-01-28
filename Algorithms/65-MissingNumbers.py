"""
Problem Statement - https://www.hackerrank.com/challenges/missing-numbers/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    D={}
    D1={}
    missing=[]
    for element in brr:
        if element not in D:
            D[element] = brr.count(element)

    for element, count in D.items():
        arr_element_count=arr.count(element)
        if arr_element_count == 0 or arr_element_count != count:
            missing.append(element)

    maximum=max(brr)
    minimum=min(brr)
    if maximum-minimum > 100:
        missing.append(maximum)
        missing.append(minimum)
 
    missing.sort()
    print(missing)
    return missing


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
