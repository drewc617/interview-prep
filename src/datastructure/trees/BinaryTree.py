class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def height(self):
        return 1

    def __str__(self):
        return str(self.val)

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if (self.root is None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if (val < node.val):
            if (node.left is None):
                node.left = Node(val)
            else:
                self._add(val, node.left) # recursive left node call
        else:
            if (node.right is None):
                node.right = Node(val)
            else:
                self._add(val, node.right) # recursive right node call

    def find(self, val):
        if self.root is None:
            return None
        else:
            return self._find(val, self.root)

    def _find(self, val, node):
        if node.val == val:
            return node
        elif val < node.val and node.left is not None:
            return self._find(val, node.left)
        elif val > node.val and node.right is not None:
            return self._find(val, node.right)

    def delete(self):
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.left)
            print str(node.val) + ' '
            self._printTree(node.right)

    def height(self):
        if self.root is None:
            return 0
        else:
            return max(self._height(self.root.left), self._height(self.root.right)) + 1

    def _height(self, node):
        if node is None:
            return 0
        else:
            return max(self._height(node.left), self._height(node.right)) + 1

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
            if r.root.left != None:
                queue.put(r.root.left)
            if r.root.right != None:
                queue.put(r.root.right) 
        return None

    


tree = BinaryTree()
tree.add(3)
tree.add(5)
tree.add(1)
tree.add(6)
tree.add(7)
tree.add(11)
tree.add(2)

print tree.height()
