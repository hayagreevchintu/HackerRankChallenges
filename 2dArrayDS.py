#Link to the challenge:
#https://www.hackerrank.com/challenges/2d-array/problem

#Stub Code:
import math
import os
import random
import re
import sys

#Solution begins here:
def hourglassSum(arr):
    max_sum = -64
    for i in range(4):
        for j in range(4):
            sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if sum > max_sum:
                max_sum = sum
    return max_sum

#Stub code:
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
