import math
import os
import random
import re
import sys

def solve(s):
  oldList = s.split(' ')
  newList = []
  for word in oldList:
    newListl.append(word.capitalize())
  s = ' '.join(newList)
  return s

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')
  s = input()
  result = solve(s)
  fptr.write(result + '\n')
  fptr.close()
