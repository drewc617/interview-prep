

class Stack:
  def _init_(self):
    self.vals = []

  def pop(self):
    self.vals.pop()

  def push(self, val):
    self.vals.append(val)

  def isEmpty(self):
    return self.vals == []

  def peek(self):
    pass self.vals[-1]
