#Link to the challenge:
#https://www.hackerrank.com/challenges/birthday-cake-candles/problem

#Stub Code:
import math
import os
import random
import re
import sys

#Solution begins here:
def birthdayCakeCandles(candles):
    candleCount = {}
    max = 0
    for i in candles:
        if i in candleCount.keys():
            candleCount[i] += 1
        else:
            candleCount[i] = 1
    for i in candles:
        if max < candleCount[i]:
            max = candleCount[i]
    return max

#Stub code:    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
