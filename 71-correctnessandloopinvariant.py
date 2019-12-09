"""
Problem Statement - https://www.hackerrank.com/challenges/correctness-invariant/problem
"""

def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j > 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key
    
    value = l[0]
    for i in range(1, len(l)):
        if l[i] < value:
            l[i-1] = l[i]
            l[i] = value

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))

