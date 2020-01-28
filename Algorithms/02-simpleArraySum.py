import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #
    # Write your code here.
    #
    sum =0
    for element in ar:
        print("initial  sum {}".format(sum))
        sum = sum + element
        print(sum, element)
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())
    print(ar_count)

    ar = list(map(int, input().rstrip().split()))
    print(ar)

    result = simpleArraySum(ar)
    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
