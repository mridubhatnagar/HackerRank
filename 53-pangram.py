"""
Problem Statement - https://www.hackerrank.com/challenges/pangrams/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

def alphabets():
    L = []
    L1=[]
    i = 65
    j=97
    while 65<=i<=90:
        L.append(chr(i))
        i=i+1
    while 97<=j<=122:
        L1.append(chr(j))
        j = j+1
    L.extend(L1)
    L.append(" ")
    return L


# Complete the pangrams function below.
def pangrams(s):
    sample_list = alphabets()
    for letter in sample_list:
        if (letter.upper() in s) or (letter.lower() in s):
            result = "pangram"
        else:
            result = "not pangram"
            break
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
