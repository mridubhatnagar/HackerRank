"""
Challenge - 31
ref link: https://www.hackerrank.com/challenges/strange-advertising/problem

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):

	share = 5
	sum = 0

	for x in range(1, n+1):

		like = math.floor(share//2)

		share = like * 3

		sum = sum + like

	print(sum)
	return sum



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    #fptr.write(str(result) + '\n')

    #fptr.close()
