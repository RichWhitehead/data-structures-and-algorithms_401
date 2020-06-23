# class Node:
class Node:
  

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
   

    def __init__(self):
      

        self.head = None

    def insert(self, value):
       

        node = Node(value)
        node.next = self.head
        self.head = node

    def __str__(self):
       

        list_str = ''
        current = self.head
        while current:
            # print(current, "current")
            list_str += str(current.value ) + ', '
            current = current.next
        return list_str[:-2]



def merge_list(list1, list2):
    """
    Merge_lists function which takes two linked lists as arguments. Zips them together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.
    """

    current1 = list1.head
    current2 = list2.head

    if current1 == None and current2 == None:
        raise Exception("lists are empty")

    if not current1:
        list1.head = list2.head
        return list1.head

    if not current2:
        return list1.head

    temp = current2.next

    while current1.next and current2.next:
        current1.next, current2.next = current2, current1.next
        current1 = current2.next
        current2, temp = temp, temp.next

    if not current1.next:
        current1.next = current2
        return list1.head

    if not current2.next:
        current1.next, current2.next = current2, current1.next
        return list1.head


