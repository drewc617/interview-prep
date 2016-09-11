#!/usr/bin/python
# Copyright 2016 Jack Chi
# LinkedList Class and common LinkedList questions
from sets import Set
class LinkedList:

    def __init__(self, val):
        self.val = val
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
            self.next = LinkedList(val)
        else:
            self.next.add(val)

    def delete(self, val):
        n = self
        if n.val is val:
            return self.next

        while n.next is not None:
            if n.next.val is val:
                n.next = n.next.next
                return self
            n = n.next
        return self

    # using a dictionary
    def removeDubplicates(self):
        uniqueVals = Set()
        previous = None
        while self is not None:
            if self.val in uniqueVals:
                previous.next = self.next
            else:
                uniqueVals.add(self.val)
                previous = self
            self = self.next
        return self

    def kthtoLast(self, k):
        if self.next is None:
            return 1

        i = self.next.kthtoLast(k) + 1
        if i is k:
            print self.val
        return i

# using 2 pointers, p2 ahead of p1 by k-1
def nthtoLast(linkedList, k):
    if k <= 0: return None
    p1 = linkedList
    p2 = linkedList

    # move p2 ahead by k
    for x in range(1,k):
        p2 = p2.next
    if p2 is None: return None

    # now move p1 & p2 at the same pace
    while p2.next is not None:
        p1 = p1.next
        p2 = p2.next
    return p1

# without access to the head
# cannot delete the last node
def deleteCurrentNode(node):
    if node is None or node.next is None:
        raise Exception("Cannot delete Node")
    next = node.next
    node.val = next.val
    node.next = next.next
    return True

