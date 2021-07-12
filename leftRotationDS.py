#Link to the challenge:
#https://www.hackerrank.com/challenges/array-left-rotation/problem

#Stub code:
import math
import os
import random
import re
import sys

#Solution begins here:
def rotateLeft(d, arr):
    for i in range(d):
        temp = arr.pop(0)
        arr.append(temp)
    return arr

#Stub code:
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = rotateLeft(d, arr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()