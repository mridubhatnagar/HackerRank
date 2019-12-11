"""
Problem Statement - https://www.hackerrank.com/challenges/beautiful-binary-string/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(b):
    i=0
    count = 0
    while i < len(b) - 2:
        if b[i]=="0" and b[i+1] == "1" and b[i+2] == "0":
            count += 1
            i += 3
        else:
            i += 1
    return count  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
