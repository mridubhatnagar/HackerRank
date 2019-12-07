"""
Problem Statement - https://www.hackerrank.com/challenges/gem-stones/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gemstones function below.
def gemstones(arr):
    D={}
    gemstone = []
    s = ''.join(arr)
    s=''.join(list(set(s)))
    for character in s:
        for word in enumerate(arr):
            position=word[0]
            value=word[1]
            if character in value: 
                if character not in D:
                    D[character] = [position]
                else:
                    D[character].append(position)
    for character in D:
        if len(D[character]) == len(arr):
            gemstone.append(character)
    return len(gemstone)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
