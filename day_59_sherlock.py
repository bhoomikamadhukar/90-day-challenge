import math
import os
import random
import re
import sys
import collections

# Complete the isValid function below.
def isValid(s):
    s=s.strip()
    freq=collections.Counter(s)
    values=list(freq.values())
    values.sort()
    result=('YES' if values.count(values[0])==len(values) or (values.count(values[0]) == len(values) -1 and values[-1] -values[-2] ==1) or (values.count(values[-1])==len(values)-1 and values[0]==1) else 'NO')
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()