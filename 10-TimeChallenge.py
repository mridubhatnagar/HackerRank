"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

Function Description

Complete the timeConversion function in the editor below. It has the following description:

Parameters	Name	Type	Description
s	String	Time in 12-hour format.
Return	The function must return a string denoting time in 24-hour format.
Raw Input Format

A single string  containing a time in -hour clock format (i.e.:  or ), where  and .

Sample Input 0

07:05:45PM
Sample Output 0

19:05:45
"""
#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    time = s[:-2]
    if 'PM' in s:
    	L=s[:-2].split(":")
    	if int(L[0]) < 12:
    	    L[0] = str(int(L[0]) + 12)
    	    time = ':'.join(L)
    	else:
    		time = s[:-2]
    	
    elif 'AM' in s:
    	L=s[:-2].split(":")
    	L[0] = str(int(L[0]) - 12)
    	if int(L[0]) >= 0:
    	    L[0] = '00'
    	    time = ':'.join(L)
    	else:
    		time = s[:-2]
    return time



if __name__ == '__main__':
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)

    #f.write(result + '\n')

    #f.close()