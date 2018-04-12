#!/bin/python3
"""
Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from  to  for three categories: problem clarity, originality, and difficulty.

We define the rating for Alice's challenge to be the triplet , and the rating for Bob's challenge to be the triplet .

Your task is to find their comparison points by comparing  with ,  with , and  with .

If , then Alice is awarded  point.
If , then Bob is awarded  point.
If , then neither person receives a point.
Comparison points is the total points a person earned.

Given  and , can you compare the two challenges and print their respective comparison points?

Input Format

The first line contains  space-separated integers, , , and , describing the respective values in triplet . 
The second line contains  space-separated integers, , , and , describing the respective values in triplet .

Constraints

Output Format

Print two space-separated integers denoting the respective comparison points earned by Alice and Bob.

Sample Input

5 6 7
3 6 10
Sample Output

1 1
""" 

import os
import sys

#
# Complete the solve function below.
#
def solve(a0, a1, a2, b0, b1, b2):
    #
    # Write your code here.
    #
    alice =0
    bob=0

    if (a0>b0):
        print("Alice scores more")
        alice = alice+1
    elif (b0 > a0):
        print("Bob score more")
        bob = bob + 1

    if (a1>b1):
        print("Alice scores more")
        alice = alice+1
    elif (b1 > a1):
        print("Bob score more")
        bob = bob + 1
 
    if (a2>b2):
        print("Alice scores more")
        alice = alice+1
    elif(b2 > a2):
        print("Bob score more")
        bob = bob + 1

    result = (alice, bob)

    return result
        

if __name__ == '__main__':
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    a0A1A2 = input().split()

    a0 = int(a0A1A2[0])

    a1 = int(a0A1A2[1])

    a2 = int(a0A1A2[2])

    b0B1B2 = input().split()

    b0 = int(b0B1B2[0])

    b1 = int(b0B1B2[1])

    b2 = int(b0B1B2[2])

    result = solve(a0, a1, a2, b0, b1, b2)
    print(result)

    #f.write(' '.join(map(str, result)))
    #f.write('\n')

    #f.close()
