# Program to implement a stack 
# copied stack over from the stack and queues lab

class Node:
  """This is the Node for instances"""
  def __init__(self, value):
    self.value = value
    self.next = None
    
class Stack:
  
  """This implements the data structure and its common methods"""
  
  def __init__(self):
    """Initiator"""
    
    self.top = None
      
  def push(self, value):
      self.top = Node(value)
    
  def pop(self):
      if self.top is None:
        raise AttributeError('The stack is empty')
      wanted = self.top
      self.top = self.top.next
      wanted.next = None
      return wanted.value
    
  def is_empty(self):
      if self.top is None:
        return True
      else:
        return False
      
  def peek(self):
      if self.top is None:
        raise AttributeError('The stack is empty')
      else:
        return self.top.value
      


class PseudoQueue:
  def __init__(stack, s1):
    self.s1 = s1
    self.s2 = Stack()
    
def enqueue(self, value):
  self.s1.push(value)
  
def dequeue(self):
  
  if self.s1.top == None:
    raise Exception('empty PseudoQueue')
  while self.s1.top != None:
    pope_file = self.s1.pop()
    
    self.s2 = self.s1.pop(poped_file)
    
    pop_val = self.s2.pop()
    
    while self.s2.top != None:
      self.s1.push(self.s2.pop())
      
      return pop_val