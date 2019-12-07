"""
Problem Setter - https://www.hackerrank.com/challenges/camelcase/problem

"""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    list_s = list(s)
    count=1
    for letter in list_s:
        ascii_value = ord(letter)
        if 65<=ascii_value<=90:
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
