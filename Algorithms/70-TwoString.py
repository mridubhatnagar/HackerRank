"""
Problem Statement - https://www.hackerrank.com/challenges/two-strings/problem
"""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    list_s1=list(s1)
    list_s2=list(s2)
    L=[]
    for character in list_s1:
        if character in s2:
            L.append(character)

    print(L)  
    if len(L)>0:
        result="YES"
    else:
        result="NO"

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
