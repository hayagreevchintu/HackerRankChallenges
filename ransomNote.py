#Link to the challenge:
#https://www.hackerrank.com/challenges/ctci-ransom-note/problem

#Stub Code:
import math
import os
import random
import re
import sys

#Solution begins here:
def checkMagazine(magazine, note):
    magazineWordCount = {}
    noteWordCount = {}
    for i in magazine:
        if i in magazineWordCount.keys():
            magazineWordCount[i] += 1
        else:
            magazineWordCount[i] = 1
    for i in note:
        if i in noteWordCount.keys():
            noteWordCount[i] += 1
        else:
            noteWordCount[i] = 1
    for i in note:
        try:
            if magazineWordCount[i] < noteWordCount[i]:
                return 'No'
        except:
            return 'No'
    return 'Yes'

#Stub Code:
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    m = int(first_multiple_input[0])
    n = int(first_multiple_input[1])
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    print(checkMagazine(magazine, note))