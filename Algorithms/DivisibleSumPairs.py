# Approach 2 Divisible Sum Pairs
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    count = 0
    for pos, val in enumerate(ar):
        for pos1, val1 in enumerate(ar):
            if pos<pos1:
                if ((val+val1)%k==0):
                    count = count + 1
    return count
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
