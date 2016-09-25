# Assume you have an array of length n initialized with all 0's and are given k update operations.
# Each operation is represented as a triplet: [startIndex, endIndex, inc] 
# which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.
# Return the modified array after all k operations were executed.
# Given:

#     length = 5,
#     updates = [
#         [1,  3,  2],
#         [2,  4,  3],
#         [0,  2, -2]
#     ]

# Output:

#     [-2, 0, 3, 5, 3]

class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        ans = [0] * length
        for update in updates:
          startIndex = update[0]
          endIndex = update[1]
          inc = update[2]
          for i in range(startIndex, endIndex+1):
            ans[i] += inc
        return ans
        