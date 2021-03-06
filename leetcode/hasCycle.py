# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution(object):
  def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    slow = head
    fast = head
    while slow is not None:
      slow = slow.next
      fast = fast.next

      if slow is None or fast is None:
        return False

      if fast.next is None:
        return False
      else: 
        fast = fast.next
      
      if slow == fast:
        return True
    return False  
