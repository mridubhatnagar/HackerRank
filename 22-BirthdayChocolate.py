"""
Output Format

Print an integer denoting the total number of ways that Lily can portion her chocolate bar to share with Ron.

Sample Input 0

5
1 2 1 3 2
3 2
Sample Output 0

2

ref link: https://www.hackerrank.com/challenges/the-birthday-bar/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(n, s, d, m):

    count=0
    
    for pos, val in enumerate(s):
        sum = 0
        if len(s) > 1:
            for j in range(pos+1, pos+m):
                if j<len(s):
                    sum = sum+s[j]
            sum = sum + val
            if sum == d:
                count=count+1
        else:
            if val == d:
                count = count+1
    print(count)
    return count

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = list(map(int, input().rstrip().split()))

    dm = input().split()

    d = int(dm[0])

    m = int(dm[1])

    result = solve(n, s, d, m)

    #fptr.write(str(result) + '\n')

    #fptr.close()
