import math
import os
import random
import re
import sys

def capitalize(s):
    return ' '.join(list(map(str.capitalize, s.split(' '))))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = capitalize(s)
    fptr.write(result + '\n')
    fptr.close()