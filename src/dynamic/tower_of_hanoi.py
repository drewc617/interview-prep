#!/usr/bin/python
# Copyright 2016 Jack Chi
# Tower Class and Tower of Hanoi problem
# Move a Stack of disks from one Tower Origin to Tower Destination using a buffer with 
# these rules:
# 1) Only 1 disk can be moved at a time
# 2) A disk is slid off the top of one tower onto another tower
# 3) A disk cannot be placed on top of a smaller disk
# 4) Using ints as disks representations

import sys

class Tower:
  def __init__(self, index):
    self.index = index
    self.disks = []

  def __str__(self):
    return "Tower[%i]: " % self.index + str(self.disks)

  def index(self):
    return self.index

  def add(self, d):
    if len(self.disks) != 0 and self.disks[-1] <= d:
      raise Exception("Illegal operation")
    else:
      self.disks.append(d)

  def moveTopTo(self, tower):
    top = self.disks.pop()
    tower.add(top)

  # move top - 1 disks to buffer, using dest as buffer
  # move top from origin to destination
  # move top-1 disks from buffer to dest using self as buffer
  def moveDisks(self, n, dest, buffer):
    if n > 0:
      self.moveDisks(n-1, buffer, dest)
      self.moveTopTo(dest)
      buffer.moveDisks(n-1, dest, self)

def main():
  n = input("Enter # of disks: ")
  
  towers = []
  for i in xrange(3):
      towers.append(Tower(i))

  for j in xrange(n,0,-1):
    towers[0].add(j)

  print towers[0]
  print towers[1]
  print towers[2]

  raw_input("Moving disks to Tower2: ")

  towers[0].moveDisks(n, towers[2], towers[1])

  print towers[0]
  print towers[1]
  print towers[2]


if __name__ == '__main__':
  main()
