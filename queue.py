#! /usr/bin/env python3
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next = next_node

class Queue:
  def __init__(self):
    self.head = self.tail = None
    self.length = 0

  def enqueue(self, value):
    node = Node(value)
    self.length += 1
    if self.tail is None:
      self.head = self.tail = node
      return
    self.tail.next = node
    self.tail = node

  def deque(self):
    if self.head is None:
      return
    self.length-=1
    head = self.head
    self.head = self.head.next
    head.next = None

  def peek(self):
    print(self.head.value)

  def show(self):
    curr = self.head
    while True:
      print(curr.value)
      if curr.next is None:
        break
      curr = curr.next

q = Queue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(5)
q.enqueue(7)
q.show()
