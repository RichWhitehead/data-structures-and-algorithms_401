class Node:
  """This is the Node for instances"""
  def __init__(self, value):
    self.value = value
    self.next = None
    
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

class Animal:
  def __init__(self, pet_name):
    self.value = pet_name
    self.next = None
    
class Cat(Animal):
  type = 'dog'
  
class Dog(Animal):
  type = 'cat'
  
class AnimalShelter:
  def __init__(self):
    self.q1 = Queue()
    self.q2 = Queue()
    
  def enqueue(self, animal):
    if isinstance(animal, Dog) or isinstance(animal, Cat):
      self.q1.enqueue(animal)
    else:
      
      return "Pet has to be dog or cat"
    
  def dequeue(self, pref):
        adopted_pet = None

        while not self.q1.is_empty():
            if self.q1.front.type == pref.lower() and adopted_pet == None:
                adopted_pet= self.queue1.dequeue()
            else:
                self.q2.enqueue(self.q1.dequeue())

        while not self.q2.is_empty():
            self.q1.enqueue(self.q2.dequeue())

        return adopted_pet
 

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
        