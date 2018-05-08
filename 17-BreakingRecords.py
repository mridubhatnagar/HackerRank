"""
Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. 
She tabulates the number of times she breaks her season record for most points and least points 
in a game. Points scored in the first game establish her record for the season, and she begins 
counting from there.

Input Format

The first line contains an integer n, the number of games. 
The second line contains n space-separated integers describing the respective values of .

Output Format

Print two space-seperated integers describing the respective numbers of times her 
best (highest) score increased and her worst (lowest) score decreased.

Sample Input 0

9
10 5 20 20 4 5 2 25 1

Sample Output 0

2 4
"""

#!/bin/python3

import os
import sys

#
# Complete the breakingRecords function below.
#
def breakingRecords(score):
    #
    # Write your code here.
    #
    highest_val = score[0]
    lowest_val = score[0]
    count_high = 0
    count_low = 0
    result = []
    for element in score:
    	if element > highest_val:
    		count_high = count_high + 1
    		highest_val = element
    	elif element < lowest_val:
    		count_low = count_low + 1
    		lowest_val = element
    result.append(count_high)
    result.append(count_low)
    return result


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    score = list(map(int, input().rstrip().split()))

    result = breakingRecords(score)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()
