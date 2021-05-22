#Stub code:
import os
import sys

#Solution begins here:
def getMoneySpent(keyboards, drives, b):
    max = 0
    for i in keyboards:
        for j in drives:
            if (i+j) > max and (i+j) <= b:
                max = i+j
    if max > 0:
        return max
    else:
        return -1

#Stub code:    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    bnm = input().split()
    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])
    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))
    moneySpent = getMoneySpent(keyboards, drives, b)
    fptr.write(str(moneySpent) + '\n')
    fptr.close()