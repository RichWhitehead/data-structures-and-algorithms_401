# Program to implement a stack 
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
      


# Implementing a queue data structure

class Queue:
  
    def __init__(self):
      """ Initiator"""
      
      self.front = None #or Node?
      # self.rear = None
      
    def enqueue(self, value):
      
      new_node = Node(value)
      
      if self.is_empty():
        self.front = new_node
        self.rear = new_node
        
      else:
        self.rear.next = new_node
        self.rear = new_node
        
      
      
    def dequeue(self):
      if self.is_empty():
        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value
      else:
        return None
      
    def peek(self):
      if self.queue is None:
        raise AttributeError('The queue is empty')
      else:
        return self.front.value
      return None

      
      

    
      
      
      
      
