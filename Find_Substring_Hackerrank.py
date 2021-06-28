#!/bin/python3
 
import math
import os
import random
import re
import sys
 
 
 
#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
 
def findSubstring(s, k):
    vowel = ["a","e","i","o","u"]
    my_max = 0
    cal_max = 0
    len_str =len(s)
    # Write your code here
    new_str = ""
    for i in range(0,len_str):
        cal_max = 0
        if((i + k) <len_str):
            for j in range(i,i+k):
                if s[j] in vowel:
                   cal_max += 1 
        if cal_max > my_max:
            index = i
            my_max = cal_max
    
    if my_max ==0:
        return "Not found!"
    else:
        return s[index:index+k]         
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
 
    s = input()
 
    k = int(input().strip())
 
    result = findSubstring(s, k)
 
    fptr.write(result + '\n')
 
    fptr.close()
