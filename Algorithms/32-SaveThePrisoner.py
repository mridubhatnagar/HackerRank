"""
Output Format

For each test case, print the chair number of the prisoner who receives the awful treat on a new line.

Sample Input 0

2
5 2 1
5 2 2
Sample Output 0

2
3

ref-link: https://www.hackerrank.com/challenges/save-the-prisoner/problem

"""


# !/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):

	next_digit = s-1
	digit_count = 1

	while digit_count >= 1 and digit_count <=m:

		digit_count = digit_count + 1

		if next_digit == n:
			next_digit = 1
		else:
			next_digit = next_digit + 1

		#print(next_digit)

	print(next_digit)
	return next_digit


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        #fptr.write(str(result) + '\n')

    #fptr.close()
