#Link to the challenge:
#https://www.hackerrank.com/challenges/extra-long-factorials/problem

#Stub code:
import math
import os
import random
import re
import sys

#Solution begins here:
def extraLongFactorials(n):
    if n == 0:
        return 1
    else:
        return n * extraLongFactorials(n-1)

#Stub code:
if __name__ == '__main__':
    n = int(input().strip())
    print(extraLongFactorials(n))