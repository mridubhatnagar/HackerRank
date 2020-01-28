"""
Problem Statement - https://www.hackerrank.com/challenges/string-construction/problem
"""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stringConstruction function below.
def stringConstruction(s):
    unique_letters = list(set(s))
    total_letters = len(unique_letters)
    return total_letters

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
