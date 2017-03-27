#!/bin/python

import sys

print "Please enter the number: "
num = int(sys.stdin.readline())

r = range(num)

print "Even numbers: "
for i in r:
  no = i + 1
  remainder = no % 2
  if remainder == 0:
    print str(no)
    
