#Link to the challenge:
#https://www.hackerrank.com/challenges/staircase/problem

#Stub Code:
import math
import os
import random
import re
import sys

#Solution begins here:
def staircase(n):
    for i in range(1,n+1):
        print((n-i)*' '+ (i*'#'))

#Stub Code:
if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)