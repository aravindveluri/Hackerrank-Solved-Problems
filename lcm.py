#!/bin/python

import math
import os
import random
import re
import sys
from itertools import combinations
# Complete the acmTeam function below.
'''def acmTeam(topic):
    maxlst = []
    for comb in enumerate(combinations(topic, 2)):
        orred = 0
        combmax = 0
        for digit in xrange(len(comb[1][0])):
            orred = int(comb[1][0][digit]) | int(comb[1][1][digit])
            if orred == 1:
                combmax += 1
        maxlst.append(combmax)
    x = max(maxlst)
    return [x, maxlst.count(x)]
'''




def acmTeam(topic):
    maxlst = []
    for comb in combinations(topic, 2):
        orred = int('1' + comb[0], 2) | int('1' + comb[1], 2)
        maxlst.append(bin(orred)[3:].count('1'))
    maxval = max(maxlst)
    return [maxval, maxlst.count(maxval)]



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in xrange(n):
        topic_item = raw_input()
        topic.append(topic_item)
    
    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    
    fptr.close()
