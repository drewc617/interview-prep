#!/usr/bin/python
# https://github.com/jackchi/interview-prep
# Copyright 2016 Jack Chi

# Directed Graph Nodes representation

from Queue import Queue

class State:
  visited, visiting, unvisited = range(3)

class Node:
  # class varaibles

  def __init__(self, val=None, children=[]):
    # instance variables
    self.val = val
    self.children = children
    self.state = State.unvisited

  def add(self, val):
    n = Node(val)
    self.children.append(n)
    return n

  def addNode(self, node):
    self.children.append(node)
    return node


def isPath(start, end):
  q = Queue()
  q.put(start)

  while (not q.empty()): 
    node = q.get()
    if node is not None:
      for adj in node.children:
        if adj.state is State.unvisited:
          if adj == end:
            return True
          else:
            adj.state = State.visiting
            q.put(adj)
      node.state = State.visited
  return False
        
taiwan = Node("taiwan")
usa = taiwan.add("usa")
japan = taiwan.add("japan")
china = taiwan.add("china")
russia = Node("russia")
uk = usa.add("uk")

print isPath(taiwan, usa)
print isPath(taiwan, uk)
print isPath(russia, taiwan)


 