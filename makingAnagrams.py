#Link to the challenge:
#https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

#stub code:
import math
import os
import random
import re
import sys

#Solution begins here:
from collections import Counter
def makeAnagram(a, b):
    # Write your code here
    count_a = Counter(a)
    count_b = Counter(b)
    count_a.subtract(count_b)
    return sum(abs(i) for i in count_a.values())

#Stub code:    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = input()
    b = input()
    res = makeAnagram(a, b)
    fptr.write(str(res) + '\n')
    fptr.close()