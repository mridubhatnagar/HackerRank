"""
For each query, return Cat A if cat  catches the mouse first, Cat B if cat  catches the mouse first, or Mouse C if the mouse escapes.

Sample Input 0

2
1 2 3
1 3 2
Sample Output 0

Cat B
Mouse C
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    

	dist_xz = abs(x - z)

	dist_yz = abs(y - z)

	if dist_xz < dist_yz:
		result = "Cat A"
	elif dist_xz == dist_yz:
		result = "Mouse C"
	else:
		result = "Cat B"

	return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)
        print(result)

        fptr.write(result + '\n')

    fptr.close()