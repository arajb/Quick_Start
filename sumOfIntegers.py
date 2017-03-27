#!/bin/python

import sys

print "Enter array of numbers like: 2 4 5 1 2"

arr = map(int, raw_input().strip().split(' '))
total = sum(arr)

print "Sum of array of integers: ", total
