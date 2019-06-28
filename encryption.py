
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the encryption function below.


    

if __name__ == '__main__':

    #s = raw_input()
    s = 'iffactsdontfittotheorychangethefacts'

    s.split()
    
    #leng = reduce(lambda x,y: len(x)+len(y), s)
    string = ''.join(s)
    leng = len(string)
    sqart = math.sqrt(leng)
    rows = 0
    columns = 0
    rows = int(sqart)
    columns = rows + 1
    if sqart%1 == 0:
    #    print sqart
        rows = columns = int(sqart)
    #    print rows,columns
    
    if leng > rows * columns:
        rows = columns
    print rows, columns
    l = []
    for i in range(columns):
        s = ''
        for j in range(rows):
            try:
                s += string[i + columns*j]
                print s
            except:
                pass
        
        l.append(s)
    for i in l:
        print i,
    
    #idtyts fooch fnthe athaf cfena tiogc stret
    print(len(s))