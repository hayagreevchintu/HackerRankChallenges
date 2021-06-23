#Link to the challenge:
#https://www.hackerrank.com/challenges/diagonal-difference/problem

#Stub Code:
import math
import os
import random
import re
import sys

#Solution begins here:
def diagonalDifference(arr):
    majorDiagonalSum = 0
    minorDiagonalSum = 0
    for i in range(len(arr)):
        majorDiagonalSum += arr[i][i]
        minorDiagonalSum += arr[i][len(arr)-i-1]
    return abs(minorDiagonalSum - majorDiagonalSum)

#Stub Code:
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()