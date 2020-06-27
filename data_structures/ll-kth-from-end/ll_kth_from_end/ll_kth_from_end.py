class Node:
    """ Class for the Node instances"""

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """ Class for the LinkedLists instances"""

    def __init__(self):
        """method to initiate a LinkedList"""

        self.head = None

    def __repr__(self):
        """method to represent that LinkedList created"""

        return "LinkedList created"

    def insert(self, value):
        """method to insert new node to the beginning of the list"""

        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self, value):
        """method to check if the given value in the liked list"""
        current = self.head
        while current:
            if current.value == value:
                return True
            else:
                current = current.next
        return False

    def __str__(self):
        """method that returns a string that represents all list elements"""

        list_str = ''
        current = self.head
        while current:
            # print(current, "current")
            list_str += str(current.value ) + ', '
            current = current.next
        
        return list_str[:-2]
    
    def kth_from_end(self, k):

        length = self.length_()

        if not -length <= k < length:
            raise Exception("k not in the range")

        step_count = None

        if k >= 0:
            step_count = length - k -1
        if k < 0:
            step_count = abs(k)-1

        current = self.head
        for _ in range(step_count):
            current = current.next
            
        return current.value
