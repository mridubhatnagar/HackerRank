"""
Problem Statement - https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem

New Concept - Subsequence in a string. Position of characters remains same.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    L1=[]
    L = ['h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k']
    j=0
    for element in L:
        for i in range(j, len(s)):
            if s[i] == element:
                L1.append(i)
                break
        j=i+1
    if len(L1) == 10:
        result = "YES"
    else:
        result = "NO"
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
