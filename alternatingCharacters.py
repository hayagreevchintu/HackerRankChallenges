#Link to the challenge:
#https://www.hackerrank.com/challenges/alternating-characters/problem

#Stub code:
import math
import os
import random
import re
import sys

#Solution begins here:
def alternatingCharacters(s):
    count = 0
    size = len(s)-1
    for i in range(0, size):
        if s[i] == s[i+1]:
            count+=1
    return count

#Stub code:
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = alternatingCharacters(s)
        fptr.write(str(result) + '\n')
    fptr.close()
