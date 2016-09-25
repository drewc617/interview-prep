# Find all non-duplicate list of integers that adds up to 0

def threeSum(nums):
  """
  type nums: List[int]
  rtype List[List[int]]
  """
  if len(nums) < 3:
    raise ValueError("Array does not have enough integers")
  nums.sort()

  ans = []
  for a in range(len(nums) - 1):
    left = a + 1
    right = len(nums) - 1

    while (left < right):
      testSum = nums[a] + nums[left] + nums[right]
      if testSum == 0:
        newEntry = [nums[a], nums[left], nums[right]]
        if not newEntry in ans:
          ans.append(newEntry)
        left += 1
      elif testSum > 0:
        right -= 1
      else:
        left += 1

  return ans


print threeSum([-1, 0, 1, 2, -1, -4])