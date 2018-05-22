"""
John works at a clothing store. He has a large pile of socks that he must pair them by color for sale.

You will be given an array of integers representing the color of each sock. Determine how many pairs of socks with matching colors there are.

John works at a clothing store and he's going through a pile of socks to find the number of matching pairs. More specifically, he has a pile of  loose socks where each sock  is labeled with an integer, , denoting its color. He wants to sell as many socks as possible, but his customers will only buy them in matching pairs. Two socks,  and , are a single matching pair if they have the same color ().

Given  and the color of each sock, how many pairs of socks can John sell?

Input Format

The first line contains an integer , the number of socks. 
The second line contains  space-separated integers describing the colors  of the socks in the pile.

Constraints

 where 
Output Format

Print the total number of matching pairs of socks that John can sell.

Sample Input

9
10 20 20 10 10 30 50 10 20
Sample Output

3
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
	"""
	Count Total Pairs
	"""
	
	# Count of each unique number
	count_dict = dict()
	pair_count = dict()
	sum = 0 

	for i in ar:
		count_dict[i] = ar.count(i)
	print(count_dict)
    
    # Possible number of pairs corresponding to each sock
	for key, values in count_dict.items():
		if values > 1:
			q, r = divmod(values, 2)
			pair_count[key] = q
	print(pair_count)


	# Total sock pairs
	for value in pair_count.values():
		sum = sum + value
    
	print(sum)
	return sum


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    #fptr.write(str(result) + '\n')

    #fptr.close()
