"""
Problem Statement - https://www.hackerrank.com/challenges/kaprekar-numbers/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    L=[]
    for number in range(p, q+1):
        square_number=number*number
        split_string = list(str(square_number))
        # right side should be d digits long
        right_side = ''.join(split_string[len(split_string)-len(str(number)):])
        # left side should be total length - d
        left_side = ''.join(split_string[:len(split_string)-len(str(number))])
        # empty string cannot be converted to int
        if right_side == '':
            right_side = 0
        elif left_side == '':
            left_side = 0
        
        # adding left side and right side should return original number
        if int(left_side) + int(right_side) == number:
            L.append(str(number))
    if len(L) == 0:
        print("INVALID RANGE")
    else:
        print(' '.join(L))



if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
