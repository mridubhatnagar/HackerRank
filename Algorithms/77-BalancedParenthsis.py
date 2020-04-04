"""
Problem Statement - https://www.hackerrank.com/challenges/balanced-brackets/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, element):
        print("inside push")
        self.items.append(element)
    
    def pop(self):
        return self.items.pop()

    def size(self):
        length = len(self.items)
        return length

    def peek(self):
        return self.items[len(self.items)-1]



def isBalanced(s):
    stack = Stack()
    result = True
    for x in s:
        if (x=='[') or (x=='(') or (x=='{'):
            stack.push(x)
        elif (x == ']') or (x == ')') or (x == '}'):
            if stack.size() > 0:    
                topmost_element = stack.pop()
                if ((topmost_element == '[') and (x != ']')) or ((topmost_element == '(') and (x != ')')) or ((topmost_element == '{') and (x != '}')):
                    result = False
                    break
                else:
                    result = True
    
    if stack.size() == 0 and result:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())
    
    for t_itr in range(t):
        s = input()
        
        result = isBalanced(s)
        print(result)

        fptr.write(result + '\n')

    fptr.close()