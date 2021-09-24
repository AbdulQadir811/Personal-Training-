#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    j  = 0
    i  = 0
    for i,x in enumerate(c):
        
        if i+2 < len(c):
            if c[i+2] == 1:
                j=j+1
                i=i+1
            elif c[i] == 0:
                i=i+2
                j=j+1    
        
    result = j
    
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
