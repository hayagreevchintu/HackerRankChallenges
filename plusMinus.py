#Link to the challenge:
#https://www.hackerrank.com/challenges/plus-minus/problem

#Stub Code:
import math
import os
import random
import re
import sys

#Solution begins here:
def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
    positiveProportion = positive/len(arr)
    negativeProportion = negative/len(arr)
    zeroProportion = zero/len(arr)
    print("{0:.6f}".format(positiveProportion))
    print("{0:.6f}".format(negativeProportion))
    print("{0:.6f}".format(zeroProportion))

#Stub Code:
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)