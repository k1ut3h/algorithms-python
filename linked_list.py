#! /usr/bin/env python3
class Node:
  def __init__(self, value=None, next_value=None):
    self.value = value
    self.next = next_value

class LinkedList:
  def __init__(self):
    self.head = self.tail = None
    self.length = 0
    return

  def append(self, value):
    node = Node(value)
    self.length+=1
    if self.head is None:
      self.head = self.tail = node
      return
    self.tail.next = node
    self.tail = node

  def prepend(self, value):
    node = Node(value)
    self.length+=1
    if self.head is None:
      self.head = self.tail = node
      return
    node.next = self.head
    self.head = node

  def get(self, idx):
    curr = self.head
    i = 0
    while i<=idx and idx<self.length:
      print(curr.value)
      if curr.next is None:
        return
      curr = curr.next
      i+=1
    print("No value at that index")

  def insert_at(self, idx, value):
    node = Node(value)
    self.length+=1
    i = 0
    curr = self.head
    while i<idx and idx<self.length:
      if curr.next is None:
        break
      curr = curr.next
      i += 1
    node.next = curr.next
    curr.next = node

  def remove(self):
    if self.head is None or self.head.next is None:
      return
    node = self.head
    self.head = self.head.next
    node.next = None

  def remove_at(self, idx):
    curr = self.head
    self.length -= 1
    i = 0
    while i<idx-1 and idx<self.length:
      if curr.next is None:
        break
      curr = curr.next
      i+=1
    node = curr.next
    curr.next = node.next
    node.next = None

  def show(self):
    curr = self.head
    while True:
      print(curr.value)
      if not curr.next:
        break
      curr = curr.next


link = LinkedList()
link.append(2)
link.append(3)
link.append(5)
link.append(7)
link.append(11)
link.insert_at(2, 69)
link.show()
link.remove()
print("--------")
link.show()
link.remove_at(2)
print("--------")
link.show()
