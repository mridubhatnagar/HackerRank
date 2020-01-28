"""
Problem Statement - https://www.hackerrank.com/challenges/strong-password/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = list("0123456789")
    lower_case = list("abcdefghijklmnopqrstuvwxyz")
    upper_case = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    special_characters = list("!@#$%^&*()-+")
    L = []
    num, lower, upper, special_char = 0, 0, 0, 0
    if n < 6:
        chars_needed = 6 - n
    else:
        for letter in password:
            print(letter)
            if (letter in numbers):
                num +=1
            elif (letter in lower_case):
                lower +=1
            elif (letter in upper_case):
                upper +=1
            elif (letter in special_characters):
                special_char +=1

        if num==0:
            L.append(num)
        if lower==0:
            L.append(lower)
        if upper==0:
            L.append(upper)
        if special_char == 0:
            L.append(special_cha)
        
        chars_needed = len(L)

    return chars_needed



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
