#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    # Initialize variables
    altitude = 0
    valley_count = 0
    in_valley = False
    
    # Iterate through each step in the path
    for step in path:
        # Update altitude based on step direction
        if step == 'U':
            altitude += 1
        else:
            altitude -= 1
        
        # Check if entering or exiting a valley
        if altitude < 0:
            if not in_valley:
                in_valley = True
        else:
            if in_valley:
                in_valley = False
                valley_count += 1
    
    return valley_count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
