"""
Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Sam’s two children, Larry and Rob, decide to play a game in which they each climb a tree and throw fruit at their (Sam’s) house. Each fruit that lands on the house scores one point for the one who threw it. Larry climbs the tree on the left (the apple), and Rob climbs the one on the right (the orange).

For simplicity, we’ll assume all of the landmarks are on a number line. Larry climbs the apple tree at point , and Rob climbs the orange tree at point . Sam’s house stands between points  and . Values increase from left to right.

You will be given a list of distances the fruits are thrown. Negative distances indicate travel left and positive distances, travel right. Your task will be to calculate the scores for Larry and Rob and report them each on a separate line.

Input Format

 space-separated integers

 and , left and right sides of Sam’s house
 space-separated integers

 and , Larry’s and Rob’s positions in the trees
 space-separated integers

 and , number of apples and oranges thrown
 space-separated integers

distances  that each apple falls from 
 space-separated integers

distances  that each orange falls from 

Sample Input
7 11
5 15
3 2
-2 2 1
5 -6


Sample Output

1  1

Explaination

The first apple falls at position  5-2=3
The second apple falls at position  5+2=7
The third apple falls at position  5+1=6
The first orange falls at position  15+5=20
The second orange falls at position  15-9=6

"""

#!/bin/python3

import os
import sys

#
# Complete the countApplesAndOranges function below.
#
def countApplesAndOranges(s, t, a, b, apples, oranges):
    #
    # Write your code here.
    #
    larry_score = 0
    bob_score = 0
    for apple in apples:
    	apple_distance = a + apple
    	print(apple_distance)
    	if (apple_distance >= s) and (apple_distance <= t):
    		larry_score = larry_score + 1

    for orange in oranges:
    	orange_distance = b + orange
    	print(orange_distance)
    	if (orange_distance >= s) and (orange_distance <= t):
    	    bob_score = bob_score + 1

    print(larry_score)
    print(bob_score)





if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apple = list(map(int, input().rstrip().split()))

    orange = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apple, orange)



