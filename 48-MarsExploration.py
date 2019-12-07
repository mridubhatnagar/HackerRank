"""
Problem Statement - https://www.hackerrank.com/challenges/mars-exploration/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    count = 0
    string_length = len(s)
    number_of_messages = int(len(s)/3)
    original_message = "SOS"*int(number_of_messages)
    L = list(original_message)
    L1 = list(s)
    for i in range(0, len(s)):
        if L[i] != L1[i]:
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
