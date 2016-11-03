#!/usr/bin/python
# https://github.com/jackchi/interview-prep
# Copyright 2016 Jack Chi

# Directed Graph Nodes representation

from enum import enum
State = Enum('visiting', 'visited', 'unvisited')

class Node:
  children = []
  val = None
  def __init__(self, val, children=[]):
    self.val = val
    self.children = children

  def add(self, val):
    n = Node(val)
    self.children.append(n)

class Graph:
  nodes = []

class SearchNode(Node):
  state = State.unvisited
  def __init__(self, val, children=[]):
    self.val = val
    self.children = children

 