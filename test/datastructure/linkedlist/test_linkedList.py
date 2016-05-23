from unittest import TestCase
from LinkedList import LinkedList

class TestLinkedList(TestCase):
    def test_constructor(self):
        val = 10
        l = LinkedList(val)
        self.assertEquals(val, l.val)

    def test_add(self):
        l = LinkedList(0)
        l.add(1)
        l.add(2)
        l.add(3)
        self.assertEquals(0, l.val)
        self.assertEquals(1, l.next.val)
        self.assertEquals(2, l.next.next.val)
        self.assertEquals(3, l.next.next.next.val)

    def test_deleteRoot(self):
        l = LinkedList(5)
        self.assertIsNone(l.delete(5))

    def test_deleteOne(self):
        l = LinkedList(1)
        l.add(2)
        l.add(3)
        l.delete(2)
        self.assertEquals(l.next.val, 3)

    def test_deleteNone(self):
        l = LinkedList(1)
        l.add(2)
        l.add(3)
        l.delete(5)
        self.assertEquals(l.val, 1)
        self.assertEquals(l.next.val, 2)
        self.assertEquals(l.next.next.val, 3)