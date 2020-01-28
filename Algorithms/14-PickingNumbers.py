"""
Given an array of integers, find and print the maximum number of integers you can select from the array such that the absolute difference between any two of the chosen integers is less than or equal to . For example, if your array is , you can create two subarrays meeting the criterion:  and . The maximum length subarray has  elements.

Input Format

The first line contains a single integer , the size of the array . 
The second line contains  space-separated integers .

Constraints

The answer will be .
Output Format

A single integer denoting the maximum number of integers you can choose from the array such that the absolute difference between any two of the chosen integers is .

Sample Input 0

6
4 6 5 3 3 1
Sample Output 0

3
Explanation 0

We choose the following multiset of integers from the array: . Each pair in the multiset has an absolute difference  (i.e.,  and ), so we print the number of chosen integers, , as our answer.

Sample Input 1

6
1 2 2 3 1 2
Sample Output 1

5
Explanation 1

We choose the following multiset of integers from the array: . Each pair in the multiset has an absolute difference (i.e., , , and ), so we print the number of chosen integers, , as our answer.

"""
#!/bin/python3

import sys

def pickingNumbers(a):
    # Complete this function
    
    a= sorted(a)
    L2=[]

    #Part 0: Iterate over the list.
    for pos, val in enumerate(a):
        L1=[]
        
        # Part 1: Add elements having difference of 1 or less. 
        # In list.
        for m in range(pos+1, len(a)):

            diff = abs(val - a[m])

            if diff <=1:
                L1.append(a[m])

        L1.append(val)
        if len(L1) > 1:
            L2.append(L1)

    x = dict()

    #Part 2: Store position of list as key, 
    # len of sublist as val
    for pos, val in enumerate(L2):
        x[pos] = len(val)


    # Part 3: Find Maximum length 
    # of subset
    max_check = []
    for values in x.values():
        max_check.append(values)

    result = max(max_check)

    return result

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = pickingNumbers(a)
    print(result)
    
