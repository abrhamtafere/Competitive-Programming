#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    for i in range(1, n):
        currentValue = arr[i]
        position = i
        while position > 0 and arr[position-1] > currentValue:
            arr[position] = arr[position-1]
            position -= 1
            print(' '.join(map(str, arr)))
        arr[position] = currentValue
        if(currentValue != arr[i]):
            print(' '.join(map(str, arr)))
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr) 
