"""
There are two kangaroos on a number line ready to jump in the positive direction (i.e, toward ). Each kangaroo takes the same amount of time to make a jump, regardless of distance. That is, if kangaroo one jumps 3 meters and kangaroo two jumps 5 meters, they each do it in one second, for example.

Given the starting locations and jump distances for each kangaroo, determine if and when they will land at the same location at the same time.

Input Format

4 space-separated integers 
: starting locations  and meters per jump  for kangaroos  and 
Output Format

Print YES if they can land on the same location at the same time. Otherwise, print NO.

Sample Input 0

0 3 4 2
Sample Output 0

YES

"""
#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
    # Complete this function

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)