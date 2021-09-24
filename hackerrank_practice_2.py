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
    temp = 0
    i  = 0
    j = 0
    for x in c:
        #if i +1 == len(c):
        #    break
        if i+1 < len(c):
            if c[i+1] == 1:
                i= i+2
                j=j+1
                print(f"1 {i} {j}")    
                      
                temp = 0
            else:
                if i+2 < len(c):
                    if c[i+2] == 1:
                        
                        i=i+1
                        j=j+1
                        print(f"2 {i} {j}")    
                      
                        temp = 0
                    else:
                        i=i+2
                        temp=temp+1
                        j=j+1
                        print(f"3 {i} {j}")    
                else: 
                    j= j+1
                    break   
                         
    
        
    result = j
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
