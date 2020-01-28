"""
Colleen is having a birthday! She will have a cake with one candle for each year of her age. When she blows out the candles, she’ll only be able to blow out the tallest ones.

Find and print the number of candles she can successfully blow out.

Input Format

integer

Colleen's age 
 space-separated integers

candle heights 
Output Format

Print the number of candles Colleen blows out.

Sample Input 0

4
3 2 1 3
Sample Output 0

2
"""
#!/bin/python3

import os
import sys

#
# Complete the birthdayCakeCandles function below.
#
def birthdayCakeCandles(n, ar):
    #
    # Write your code here.
    #
    
    maximum_element = max(ar)
    count_element = ar.count(maximum_element)
    print(count_element)
if __name__ == '__main__':
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(n, ar)

    #f.write(str(result) + '\n')

    #f.close()
