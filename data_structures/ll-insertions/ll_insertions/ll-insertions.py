# this method appends 

def append_O1(self, item):
        temp = Node(item)
        last = self.tail
        last.setnext(temp)
        self.tail = temp
        self.length += 1


# this method inserts the value before

def insertBefore (self, item):
    newNode = Node(item)
    newNode.setdata(item)
    
    if self.listLength() == 0:
        self.head = newMode
    else:
      newNode.setnext(self.head)
      self.head = newNode
      
# this method inserts the value after

def insertAfter(self, item):
    newNode = Node(item)
    newNode.setdata(item)
    current = self.head
    while current.getnext() != None:
        current = current.getnext()
    current.setnext(newNode)

    