"""
Print the full date of Day of the Programmer during year  in the format dd.mm.yyyy, where dd is the two-digit day, mm is the two-digit month, and yyyy is .

Sample Input 0

2017
Sample Output 0

13.09.2017

ref-link: https://www.hackerrank.com/challenges/day-of-the-programmer/problem

"""

#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the solve function below.
def solve(year):

    sum = 0

    #Part 0: Julian and Gregorian Calender
    # Part 1 Check weather the year is leap year or not. Accordingly vary days in feb
    if (year >= 1700 and year <= 1917):
    	print("Julian")
    	if (year%4==0):
    		feb = 29
    	else:
    		feb = 28

    elif (year > 1918):
        print("Gregorian")   
        if (year%400==0) or (year%4==0 and year%100!=0):
            feb = 29
        else:
            feb = 28
    elif (year == 1918):
    	feb = 15


    # Part 2 Computes total days 31+feb+30+31 ..........
    for month in range(1, 12+1):

        if month == 2:
            sum = sum + feb

        elif (month%2 == 0) and (month != 8 and month!=12):
            sum = sum + 30
        else:
            sum = sum + 31

        print("Sum is ", sum)

        days = 256 - sum
    
        # Part 3 Find the 256th day
        if days >= 1 and days <=31:
            #days = sum - 256
            #print("date is ", days)
            # Date string formatting
            month = month + 1
            if len(str(month))<2:
                month = "0"+str(month)
            elif len(str(days))<2:
                days = "0"+days
            date_string = str(days) + '.' + str(month) + '.' + str(year)
            break

    print(date_string)



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input())

    result = solve(year)

    #fptr.write(result + '\n')

    #fptr.close()