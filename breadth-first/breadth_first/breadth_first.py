def breadth_first(tree, node = None, array = None):
    q = Queue
    if array is None:
      array = []
    if tree.root:
        q.enqueue(tree._root)
        
    while q.peek():
      node_front = q.dequeue()
      array.append(node_front.value)
      
      if node_front.left:
        q.enqueue(node_front.left)
      if node_front.right:
        q.enqueue(node_front.right)
        
    return node
        
      