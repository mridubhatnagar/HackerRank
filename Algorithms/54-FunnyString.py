"""
Problem Statement - https://www.hackerrank.com/challenges/funny-string/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    ascii_original = []
    ascii_reverse = []
    L1, L = [], []
    reverse_s = s[::-1]
    for x in s:
        ascii_original.append(ord(x))
    for x in reverse_s:
        ascii_reverse.append(ord(x))
    for i in range(0, len(ascii_original)-1):
        L.append(abs(ascii_original[i+1]-ascii_original[i]))
        L1.append(abs(ascii_reverse[i+1]-ascii_reverse[i]))
    for i in range(0, len(L)):
        if L[i] != L1[i]:
            result = "Not Funny"
            break
        else:
            result = "Funny"
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
