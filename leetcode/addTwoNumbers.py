# You are given two linked lists representing two non-negative numbers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
       self.val = x
       self.next = None

  def __str__(self):
      if self.val is None:
          return ''
      elif self.next is None:
          return str(self.val)
      else:
          return str(self.val) + '->' + self.next.__str__()

  def add(self, val):
      if not self.next:
        self.next = ListNode(val)
      else:
        self.next.add(val)
                  
class Solution(object):
  def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    dummy = ListNode(0)    
    p,q,carry,current = l1,l2,0,dummy
    while(p is not None or q is not None):
      x = p.val if p is not None else 0
      y = q.val if q is not None else 0
      sum = x + y + carry
      carry = sum / 10
      current.next = ListNode(sum % 10)
      current = current.next
      p = p.next if p is not None else None
      q = q.next if q is not None else None
    if (carry):
      current.next = ListNode(carry)  
    return dummy.next

l1 = ListNode(2)
l1.add(4)
l1.add(3)
print l1
# 2->4->3
l2 = ListNode(5)
l2.add(6)
l2.add(4)
print l2
# 5->6->4

s = Solution()
print s.addTwoNumbers(l1, l2)
