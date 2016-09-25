# Pairs should not contain duplicates
# two-pointers

def pairSum(array, sum):
  """
  :type k: Int sum we are looking for
  :rtype: List[List[int]] All pairs adding up to sum
  """
  if len(array) < 2:
    return
  array.sort() # n(logn) time complexity

  left, right = (0, len(array)-1)
  pairs = []
  while(left < right):
    currentSum = array[left] + array[right]
    if currentSum == sum:
      if not (array[left], array[right]) in pairs:
        pairs.append((array[left], array[right]))
      left+=1
    elif currentSum < sum:
      left+=1
    else:
      right-=1
  return pairs

array = [3,2,0,-2,-1,0,-1,1,4,5,6]
print pairSum(array, 5)
