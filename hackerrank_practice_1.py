#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, A):
    # Write your code here
    for i in range(len(A)):
      
    # Find the minimum element in remaining 
    # unsorted array
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
                    
        # Swap the found minimum element with 
        # the first element        
        A[i], A[min_idx] = A[min_idx], A[i]
    print(A)    
    s=1
    s2=0
    print(len(A))
    for i,x in enumerate(A):
        if (i+1) < len(A):
            if A[i] == A[i+1]:
                s=s+1
            else:
                s2=s2+(s//2)
                s=1
            
    s2=s2+(s//2)                
    return s2           

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
