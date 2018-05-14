"""
You are given an array of  integers, , and a positive integer, . Find and print the number of  pairs where  and  +  is divisible by .

Input Format

The first line contains  space-separated integers,  and . 
The second line contains  space-separated integers describing the values of .

Constraints

Output Format

Print the number of  pairs where  and  +  is evenly divisible by .

Sample Input

6 3
1 3 2 6 1 2
Sample Output

 5

"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
	count = 0
	for i in range(len(ar)):
		for j in range(len(ar)):
			if i<j:
				if ((ar[i]+ar[j])%k==0):
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
