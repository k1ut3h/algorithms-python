#! /usr/bin/env python3
class Node:
  def __init__(self, value=None, prev_node=None):
    self.value = value
    self.prev = prev_node

class Stack:
  def __init__(self):
    self.head = None
    self.length = 0

  def push(self,value):
    node = Node(value)
    self.length+=1
    if self.head is None:
      self.head = node
      return
    node.prev = self.head
    self.head = node

  def pop(self):
    self.length -= max(0, self.length-1)
    if self.length == 0:
      self.head = None
      return
    head = self.head
    self.head = head.prev

  def peek(self):
    print(self.head.value)

  def show(self):
    curr = self.head
    while True:
      print(curr.value)
      if curr.prev is None:
        break
      curr = curr.prev


stack = Stack()
stack.push(2)
stack.push(3)
stack.push(5)
stack.push(7)
stack.show()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
