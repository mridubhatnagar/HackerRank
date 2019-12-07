"""
Output Format

Print an integer denoting the minimum number of pages Brie must turn to get to page .

Sample Input 0

6
2
Sample Output 0

1

ref link: https://www.hackerrank.com/challenges/drawing-book/problem

"""
#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
