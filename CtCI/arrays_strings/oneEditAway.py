#!/usr/bin/python
# https://github.com/jackchi/interview-prep
# Copyright 2016 Jack Chi

'''
One Edit Away: There are 3 types of edits that can be performed on a String
1. insert 2. update 3. remove. Given 2 strings, write a function to check if they are 
one edit away

Example:
pale, ple -> true
pales, pale -> true
pales, bale -> false
pale, bale -> false
paleo, ball -> false
'''

# if you can update one character in s1 to make s2
def oneUpdateAway(s1, s2):
  foundDifference = False
  for i in xrange(len(s1)):
    if s1[i] != s2[i]:
      if foundDifference:
        return False
      foundDifference = True
  return True  

# if you can remove one character in s1 to make s2
def oneRemoveAway(longer, shorter):
  idx1, idx2 = 0,0
  while (idx1 < len(longer) and idx2 < len(shorter)):
    if longer[idx1] != shorter[idx2]:
      if idx1 != idx2:
        return False
      idx1 += 1
    else:
      idx1 += 1  
      idx2 += 1  
  return True

# one edit away s1 from s2
def oneEditAway(s1, s2):
  if len(s1) == len(s2) and s1 != s2: # same string is not one edit away
    return oneUpdateAway(s1, s2)
  elif len(s1) + 1 == len(s2):
    return oneRemoveAway(s2, s1)
  elif len(s2) + 1 == len(s1):
    return oneRemoveAway(s1, s2)
  else:
    return False

import unittest

class TestOneEditAway(unittest.TestCase):
  
  def setUp(self):
    self.updates_pairs_true = [('bale', 'pale'), ('man', 'ban'), ('loser', 'poser')]
    self.updates_pairs_false = [('wine', 'beer'), ('tea', 'pee'), ('jack', 'mark')]
    self.remove_pairs_true = [('pale', 'ple'), ('bali', 'bal'), ('player', 'playr')]
    self.remove_pairs_false = [('pale', 'pie'), ('bali', 'pal'), ('player', 'playa')]
    self.edit_pairs_false = [('pumpkin', 'pumpkin'), ('cali', 'california'), ('coffee', 'offer')]

  def test_update_true(self):
    for p in self.updates_pairs_true:
      self.assertTrue(oneUpdateAway(p[0], p[1]))

  def test_update_false(self):
    for p in self.updates_pairs_false:
      self.assertFalse(oneUpdateAway(p[0], p[1]))

  def test_remove_true(self):
    for p in self.remove_pairs_true:
      self.assertTrue(oneRemoveAway(p[0], p[1]))

  def test_remove_false(self):
    for p in self.remove_pairs_false:
      self.assertFalse(oneRemoveAway(p[0], p[1]))

  def test_edit_true(self):
    for p in self.updates_pairs_true + self.remove_pairs_true:
      self.assertTrue(oneEditAway(p[0], p[1]))

  def test_edit_false(self):
    for p in self.edit_pairs_false:
      self.assertFalse(oneEditAway(p[0], p[1]))

if __name__ == '__main__':
  unittest.main()