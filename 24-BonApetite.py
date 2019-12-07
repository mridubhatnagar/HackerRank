"""
If Brian did not overcharge Anna, print Bon Appetit on a new line; otherwise, print the difference (i.e., ) that Brian must refund to Anna. This will always be an integer.

Sample Input 0

4 1
3 10 2 9
12
Sample Output 0

5
"""

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(n, s, d):
    
    sum=0
    not_included = n[1]
    bill_charges = s.remove(s[not_included])
    for i in s:
        sum = sum + i
    paid_charge = int(sum/2)
    over_charge = b - paid_charge
    if over_charge > 0:
        print(over_charge)
        amount = over_charge
    else:
    	print("Bon Appetit")
    	amount = "Bon Appetit"
    return amount


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = list(map(int, input().rstrip().split()))

    s = list(map(int, input().rstrip().split()))

    b = int(input())

    result = solve(n, s, b)
    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()