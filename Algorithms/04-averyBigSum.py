"""
Function Description

Complete the function aVeryBigSum in the editor below. It has the following description:

Parameters	Name	Type	Description
n	Integer	Number of elements in the input array.
ar	LongInteger Array	Array elements whose sum needs to be computed.
Return	The function must return a long integer denoting sum of all array elements.
Constraints

Raw Input Format

The first line of the input consists of an integer . 
The next line contains  space-separated integers contained in the array.

Sample Input 0

5
1000000001 1000000002 1000000003 1000000004 1000000005
Sample Output 0

5000000015
Note:

The range of the 32-bit integer is .
When we add several integer values, the resulting sum might exceed the above range. You might need to use long long int in C/C++ or long data type in Java to store such sums.
"""

#!/bin/python3

import os
import sys

#
# Complete the aVeryBigSum function below.
#
def aVeryBigSum(n, ar):
    #
    # Write your code here.
    #
    sum =0
    for element in ar:
        print("initial  sum {}".format(sum))
        sum = sum + element
        print(sum, element)
    return sum

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(n, ar)

    f.write(str(result) + '\n')

    f.close()


