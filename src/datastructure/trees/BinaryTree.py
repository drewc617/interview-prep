#!/usr/bin/python
# https://github.com/jackchi/interview-prep
# Copyright 2014 Jack Chi

# Binary Tree Nodes Representation
# Using Nodes and References to model a Binary Tree

import Queue


def isLeaf(node):
    return not node.getLeftChild() and not node.getRightChild()

def insert(val, leftLine, rightLine, line):
    print "%d %s %d %d" % (line, val, leftLine, rightLine)
    return line

class BinaryTree:

    def __init__(self, rootVal=None):
        self.val = rootVal
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newVal):
        if not self.leftChild:
            self.leftChild = BinaryTree(newVal)
        else:
            t = BinaryTree(newVal)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newVal):
        if not self.rightChild:
            self.rightChild = BinaryTree(newVal)
        else:
            t = BinaryTree(newVal)
            t.rightChild = self.rightChild
            self.rightChild = t

    def insert (self, newVal):
        prev = None
        curr = self
        while curr:
            prev = curr
            if newVal < curr.val:
                curr = curr.leftChild
            else:
                curr = curr.rightChild  
        if newVal < prev.val:
            prev.leftChild = BinaryTree(newVal)
        else:
            prev.rightChild = BinaryTree(newVal)


    def getLeftChild(self):
        return self.leftChild       

    def getRightChild(self):
        return self.rightChild      

    def setRootVal(self, val):
        self.val = val

    def getRootVal(self):
        return self.val

    @staticmethod   
    def getHeight(node):
        if node == None:
            return 0
        else: 
            return max(BinaryTree.getHeight(node.getLeftChild()), 
                    BinaryTree.getHeight(node.getRightChild())) + 1 

    def BFSearch(self, target):
        """ Using a Queue to iteratively search adjacent nodes
        before traversing down the tree
        """

        queue = Queue.Queue()
        queue.put(self)
        
        while not queue.empty():
            r = queue.get()
            if (r.val == target):
                return r
            if r.leftChild != None:
                queue.put(r.leftChild)
            if r.rightChild != None:
                queue.put(r.rightChild) 
        return None

    def DFSearch(self, target):
        """ Using recursion to search leftmost depth nodes
        before traversing across adjacent nodes
        """
        if self.val == target:
            return self
        else:
            if not self.getLeftChild():
                self.getLeftChild().DFSearch(target)
            if not self.getRightChild():
                self.getRightChild().DFSearch(target)

    def DFPrint(self, line=0):
        if isLeaf(self):
            line+=1
            return insert(self.val, -1, -1, line)       
        else: 
            line+=1
            return insert(self.val, self.getLeftChild().DFPrint(line) if self.getLeftChild() else -1, 
                self.getRightChild().DFPrint(line) if self.getRightChild() else -1, line) 


