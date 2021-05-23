#Stub code:
import math
import os
import random
import re
import sys

#Sample code:
def timeConversion(s):
    am_or_pm = s[-2:]
    s = s[:-2].split(':')
    if am_or_pm == 'AM':
        if s[0] == '12':
            s[0] = '00'
    elif am_or_pm == 'PM':
        if int(s[0]) < 12:
            s[0] = str(int(s[0])+12)
    return ':'.join(s)

#Stub code:
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    print(result)
    fptr.write(result + '\n')
    fptr.close()