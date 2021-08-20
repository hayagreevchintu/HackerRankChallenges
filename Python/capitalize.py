#Link to the challenge:
#https://www.hackerrank.com/challenges/capitalize/problem

#Stub code:
import math
import os
import random
import re
import sys

#Solution begins here:
def capitalize(s):
    return ' '.join(list(map(str.capitalize, s.split(' '))))

#Stub code:
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = capitalize(s)
    fptr.write(result + '\n')
    fptr.close()
