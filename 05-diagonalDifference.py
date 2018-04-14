import os
import sys

"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

Function Description

Complete the diagonalDifference function in the editor below. It has the following description:

Parameters  Name    Type    Description
a   2D Integer Array    The elements in the matrix
Return  An integer denoting the absolute difference between the two sums of the matrix's diagonals.
Constraints

Raw Input Format

The first line contains a single integer, n denoting the number of rows and columns in the matrix a. 
The next  lines denote the matrix a's rows, with each line containing n space-separated integers describing the columns.

"""


#
# Complete the diagonalDifference function below.
#
def diagonalDifference(a):
    #
    # Write your code here.
    #
    print(len(a))

    left_diagonal_sum = 0
    right_diagonal_sum = 0
    for x in range(len(a)):
        left_diagonal_sum = left_diagonal_sum + a[x][x]
        right_diagonal_sum = right_diagonal_sum + a[x][((len(a)-1)-x)]
    print(left_diagonal_sum, right_diagonal_sum)
    absolute_value = abs(left_diagonal_sum - right_diagonal_sum)
    print(absolute_value)
    return absolute_value

        
if __name__ == '__main__':
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)
    print(result)

    #f.write(str(result) + '\n')

    #f.close()
