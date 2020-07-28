def find_maximum_value(self):
        """ An instance method that returns the maximum value stored in the tree"""

        q = Queue()
       
        if not self._root:
            return None

        max_ = self._root.value
        q.enqueue(self._root)

        while not q.is_empty():
            node_front = q.dequeue()

            max_ = max(max_, node_front.value)


            if node_front.left:
                q.enqueue(node_front.left)
            if node_front.right:
                q.enqueue(node_front.right)

        return max_



class myException(Exception):
    pass

