# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true
import string

def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    sIndex = 0
    for t in p:
      if isLetters(t):
        prev = t
        if (s[sIndex] != t):
          return False
        else:
          sIndex += 1
      elif isPeriodMatch(t):
        
    return

def isPeriodMatch(c):
  return len(c) == 1 and c not in ["\r", "\n"]

def isLetters(c):
  return c in string.ascii_letters

print isPeriodMatch("lkajsdf;lajds;laj")
print isPeriodMatch("j")
print isPeriodMatch("4")
print isPeriodMatch("")
print isPeriodMatch(".")
print isPeriodMatch(")")

