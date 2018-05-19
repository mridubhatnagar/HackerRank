"""
Monica wants to buy a keyboard and a USB drive from her favorite electronics store. The store has several models of each. Monica wants to spend as much as possible for the  items, given her budget.

Given the price lists for the store's keyboards and USB drives, and Monica's budget, find and print the amount of money Monica will spend. If she doesn't have enough money to both a keyboard and a USB drive, print -1 instead. She will buy only the two required items.

For example, suppose she has  to spend. Three types of keyboards cost . Two USB drives cost . She could purchase a , or a . She chooses the latter. She can't buy more than  items so she can't spend exactly .

Input Format

The first line contains three space-separated integers , , and , her budget, the number of keyboard models and the number of USB drive models. 
The second line contains  space-separated integers , the prices of each keyboard model. 
The third line contains  space-separated integers , the prices of the USB drives.

Constraints

The price of each item is in the inclusive range .
Output Format

Print a single integer denoting the amount of money Monica will spend. If she doesn't have enough money to buy one keyboard and one USB drive, print -1 instead.

Sample Input 0

10 2 3
3 1
5 2 8
Sample Output 0

9
Explanation 0

She can buy the  keyboard and the  USB drive for a total cost of .

"""
#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #

    #Part One: Finding sum of 2 items one 1 keyboard, 1 USB drive
    keyboards_drives = []
    for position, value in enumerate(keyboards):
        for drive_pos, drive_val in enumerate(drives):
            sum = value + drive_val
            if sum <= b:
                keyboards_drives.append(sum)
    print(keyboards_drives)

    #If price is greater than budget print -1 else 1
    if len(keyboards_drives) !=0:
        print(max(keyboards_drives))
        output = max(keyboards_drives)
    else:
        print("-1")
        output = -1

    return output
   


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    #fptr.write(str(moneySpent) + '\n')

    #fptr.close()
