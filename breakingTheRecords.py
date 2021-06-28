#Link to the challenge:
#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

#Stub code:
import math
import os
import random
import re
import sys

#Solution begins here:
def breakingRecords(scores):
    min = 99999999999
    max = -1
    brokenRecords = [-1] * 2
    for i in scores:
        if i < min:
            min = i
            brokenRecords[1] += 1
        if i > max:
            max = i
            brokenRecords[0] += 1
    for i in range(2):
        if brokenRecords[i] == -1:
            brokenRecords[i] = 0
    return brokenRecords

#Stub code:
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()