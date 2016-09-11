#!/usr/bin/python
# Given an array of integers and a target integer
# Find the two indices that sums up to target
# Assume only 1 answer exist 

def twoSums(nums, target):
  for index1 in range(len(nums)):
    for index2 in range(index1+1,len(nums)):
      if nums[index1] + nums[index2] == target:
        return [index1, index2]
  return []

print twoSums([4,2,3], 5)
print twoSums([4,2,3], 6)
print twoSums([4,2,3], 7)