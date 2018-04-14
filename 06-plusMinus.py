"""
Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

Input Format

The first line contains an integer, , denoting the size of the array. 
The second line contains  space-separated integers describing an array of numbers .

Output Format

You must print the following  lines:

A decimal representing of the fraction of positive numbers in the array compared to its size.
A decimal representing of the fraction of negative numbers in the array compared to its size.
A decimal representing of the fraction of zeros in the array compared to its size.
Sample Input

6
-4 3 -9 0 4 1         
Sample Output

0.500000
0.333333
0.166667
Explanation

There are  positive numbers,  negative numbers, and  zero in the array. 
The proportions of occurrence are positive: , negative:  and zeros: .
"""

import os
import sys

#
# Complete the plusMinus function below.
#
def plusMinus(arr):
    #
    # Write your code here.
    #
    positive = 0
    negative = 0
    zero = 0
    for element in arr:
    	if element < 0:
    		negative += 1
    	elif element > 0:
    		positive += 1
    	elif element == 0:
    		zero +=1
    print(positive, negative, zero)

    # Proportion of occurance
    positive_fraction = positive/len(arr)
    print("%.6f" %(positive_fraction))
    negative_fraction = negative/len(arr)
    print("%.6f" %(negative_fraction))
    zero_fraction = zero/len(arr)
    print("%.6f" %(zero_fraction))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
