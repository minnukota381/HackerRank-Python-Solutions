#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    k = s.split(" ")
    
    capitalized_words = []
    
    for i in k:
        capitalized_words.append(i.capitalize())
    
    return ' '.join(capitalized_words)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
