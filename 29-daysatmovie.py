"""
Output Format

Print the number of beautiful days in the inclusive range between  and .

Sample Input

20 23 6
Sample Output

2

ref link: https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):

	
	L=[]
	L1=[]
    
    # Part 0: Iterate over defined range
	for x in range(i, j+1):
		m = x

		#Part 1: Reverse the number
		reverse_num = 0
        
		while(x > 0):
			quotient, remainder = divmod(x, 10)
			x = quotient
			reverse_num = int(reverse_num*10) + int(remainder)
			
		# Part2: Difference between number and reverse number	
		value = abs(m-reverse_num)


		# Part 3: If returned no is whole number append, else don't
		if value%k == 0:
			q = value//k
			L1.append(q)
		else:
			q = value/k

	
	result = len(L1)
	print(result)

	return result


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    #fptr.write(str(result) + '\n')

    #fptr.close()
