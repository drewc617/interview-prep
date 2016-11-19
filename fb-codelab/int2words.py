#!/usr/bin/python
# https://github.com/jackchi/interview-prep

# Given any integer(negative included),print an English phrase that describes the integer
# 0 = "Zero" 
# 45 = "Fourty Five"
# 1,674 = "One Thousand Six Hundred Seventy Four"
# 4,000,500 = "4 Million Five Hundred"

# convert(19,323,984) = convert(19) + " Million " + convert(323) + " Thousand " + convert(984)

negative = "Negative"

smalls = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
"Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

tens = ["", "", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

hundred = "Hundred"

bigs = ["", "Thousand", "Million", "Billion"]

bigs.append

def listToString(parts):
  return reduce(lambda x, y: x + " " + y, parts)

def convertChunk(num):
  parts = []

  # converts hundreds place
  if num >= 100:
    parts.append(smalls[num / 100])
    parts.append(hundred)
    num = num % 100  

  # converts tens place
  if num >= 10 and num <= 19:
    parts.append(smalls[num])
  elif num >= 20:
    parts.append(tens[num / 10])
    num = num % 10
  
  # converts ones place
  if num >= 1 and num <= 9:
    parts.append(smalls[num])

  return listToString(parts)

def convert(num):
  if num == 0:
    return smalls[0]
  elif num < 0:
    return negative + " " + convert(-1*num)

  parts = []  
  counter = 0
  while(num > 0 ):
    if num % 1000 != 0:
      chunk_string = convertChunk(num % 1000) + " " + bigs[counter]
      parts.insert(0, chunk_string) # add to front
    num = num / 1000
    counter = counter + 1

  return listToString(parts).rstrip()

# Test
import unittest

class TestInt2Words(unittest.TestCase):
  def setUp(self):
    self.chunkPairs = [("One Hundred Fourty Five", 145), ("Five", 5), 
                        ("Sixteen", 16), ("Ninety Nine", 99), ("Eighteen", 18),
                        ("Seventy One", 71), ("Seven Hundred Thirty Three", 733)]
    self.pairs = [("Zero", 0), ("Negative Four", -4), ("Seven Thousand Eight Hundred", 7800), 
    ("Six Million Nine Hundred Thousand Seventy Five", 6900075)]

  def test_convertChunk(self):
    for p in self.chunkPairs:
      self.assertEquals(p[0], convertChunk(p[1]))

  def test_convert(self):
    for p in self.pairs:
      self.assertEqual(p[0], convert(p[1]))

if __name__ == '__main__':
    unittest.main()
