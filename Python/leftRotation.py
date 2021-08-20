#Link to the challenge:
#https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

#Stub code:
import math
import os
import random
import re
import sys

#Solution begins here:
def rotLeft(a, d):
    for i in range(d):
        temp = a.pop(0)
        a.append(temp)
    return a

#Stub code:
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    a = list(map(int, input().rstrip().split()))
    result = rotLeft(a, d)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
