#!/usr/bin/python
# https://github.com/jackchi/interview-prep
# Copyright 2016 Jack Chi

'''
Write a function to count the number of 2s that appear in all numbers between
0 & n (inclusive)

Example:
Input 25:
Output 9:
(2,12,20,21,22,23,24,25)

Hint#:
Count the numbers of 2s in each digit (for each number)

Recognizing that for every digit there are 3 categories
1. digits < 2 : 1/10 of all numbers up to roundedDown power of ten 
2. digits == 2 : previous plus everything up to that number
3. digits > 2 : 1/10 of all numbers up to roundedUp power of ten
'''

def countTwos(num):
  count = 0
  for i in xrange(len(str(num))):
    count += count2sInDigit(num, i)
  return count

def count2sInDigit(num, d):
  powerOf10 = 10 ** d
  nextPowerOf10 = 10 * powerOf10
  right = num % powerOf10

  roundDown = num - (num % nextPowerOf10)
  roundUp = roundDown + nextPowerOf10

  digit = (num / powerOf10) % 10
  if digit < 2:
    return roundDown / 10
  elif digit == 2:
    return roundDown / 10 + right + 1
  else:
    return roundUp / 10

print countTwos(25)
