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
