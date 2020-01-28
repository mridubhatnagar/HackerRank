"""
You have been asked to help study the population of birds migrating across the continent. 
Each type of bird you are interested in will be identified by an integer value. 
Each time a particular kind of bird is spotted, its id number will be added to your array 
of sightings. You would like to be able to find out which type of bird is most common 
given a list of sightings. Your task is to print the type number of that bird and if two 
or more types of birds are equally common, choose the type with the smallest ID number.

Input Format

The first line contains an integer denoting n, the number of birds sighted and reported in the array ar. 
The second line describes ar as n  space-separated integers representing the type numbers of each bird 
sighted.

Output Format

Print the type number of the most common bird; if two or more types of birds are equally common, choose the type with the smallest ID number.

Sample Input 0

6
1 4 4 4 5 3
Sample Output 0

4
"""

#!/bin/python3

import os
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(n, ar):
    
    freq_dict = {}
    for element in ar:
        count = ar.count(element)
        freq_dict[element] = count
    result = max(freq_dict, key=freq_dict.get)
    
    return result


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = migratoryBirds(ar_count, ar)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
