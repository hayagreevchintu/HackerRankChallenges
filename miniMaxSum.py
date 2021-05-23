#Link to the challenge:
#https://www.hackerrank.com/challenges/mini-max-sum/problem

#Stub code:
import math
import os
import random
import re
import sys

#Solution begins here:
def miniMaxSum(arr):
    sum_arr = sum(arr)
    print(str(sum_arr - max(arr)) + ' '+ str(sum_arr- min(arr)))

#Stub code:
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
