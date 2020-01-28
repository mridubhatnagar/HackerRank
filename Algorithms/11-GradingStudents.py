"""
At HackerLand University, a passing grade is any grade 40 points or higher on a 100 point scale. Sam is a professor at the university and likes to round each student’s grade according to the following rules:

If the difference between the grade and the next higher multiple of 5 is less than 3, round to the next higher multiple of 5
If the grade is less than 38, don’t bother as it’s still a failing grade
Automate the rounding process then round a list of grades and print the results.

Input Format

First Line

integer 
: number of students
Next  lines

integer 
: individual grades
Output Format

Print  lines, each with the rounded value of a student’s grade in input order.

Sample Input 0

4
73
67
38
33
Sample Output 0

75
67
40
33
Explanation 0

The first grade,  is two below the next higher multiple of , so it rounds to . 
 is  points less than the next higher multiple of  so it doesn’t round. 
, like , rounds up to next higher multiple of , or  in this case. 
 is less than , so it does not round.

"""
#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    #
    # Write your code here.
    #
    L=[]
    for marks in grades:
    	if ((marks+1)%5 == 0) and ((marks+1) > 38):
    		L.append(marks+1)
    	elif ((marks+2)%5 == 0) and ((marks+2) > 38):
    		L.append(marks+2)
    	else:
    		L.append(marks)
    
    return L


if __name__ == '__main__':
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    for marks in result:
    	print(marks)


    #f.write('\n'.join(map(str, result)))
    #f.write('\n')

    #f.close()
