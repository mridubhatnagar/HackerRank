#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    i, j = divmod(n, c)
    print(i, j)
    total = i
    if total == m:
        total = total + 1
        print(total)
    else:
        while i > m:
           k, z = divmod(i, c)
           total = total + k
           i = k
           print(k, z, total)
           print(total)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
