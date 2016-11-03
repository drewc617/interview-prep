class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = {}    # store position of each character in the substring
        start = 0  # store position of the start of each substring
        longest = 0   # length of longest substring 
        for i, c in enumerate(s):
          if c in index:
            # current c is in index
            # find the new start
            start = max(start, index[c] + 1)
          index[c] = i 
          # compare longest with current substring
          longest = max(longest, i - start + 1)
        return longest
          
s = Solution()
print s.lengthOfLongestSubstring("abcabcbb")
print s.lengthOfLongestSubstring("aab")