"""
Output Format

For each test case, print the word YES if the class is canceled or NO if it is not.

Note 
If a student arrives exactly on time , the student is considered to have entered before the class started.

Sample Input

2
4 3
-1 -3 4 2
4 2
0 -1 2 1
Sample Output

YES
NO

ref link: https://www.hackerrank.com/challenges/angry-professor/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):

	count_pos = 0
	count_neg = 0

	for i in a:
		if i <=0:
			count_neg = count_neg  + 1
		else:
			count_pos = count_pos + 1

	if count_neg < k:
		result = "YES"
	else:
		result = "NO"

	return result

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)
        print(result)

        #fptr.write(result + '\n')

    #fptr.close()