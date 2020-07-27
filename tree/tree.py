class Node(object):
  
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    
class BinaryTree(object):
  def __init__(self, root):
    self.root = Node(root)
    
    
  def print_tree(self, traversal_type):
    if traversal_type == "preOrder":
      return self.preOrder(tree.root)
    elif traversal_type == "inOrder":
      return self.inOrder(tree.root)
    elif traversal_type == "postOrder":
      return self.postOrder(tree.root)
    else:
      print("Traversal type" + str(traversal_type) + "is not supported.")
    
# This method will preOrder: Root --> Left --> Right 12453678

  def preOrder(self, start):
    traversal = ""
    if start:
        traversal += (str(start.value) + "") 
        traversal += self.preOrder(start.left)
        traversal += self.preOrder(start.right)
       
    return traversal
# This method will inOrder: Left--> Root --> Right  42516378
  def inOrder(self, start):
    traversal = ""
    if start:
        traversal += self.inOrder(start.left)
        traversal += (str(start.value) + "") 
        traversal += self.inOrder(start.right)
    return traversal
  
# This method will postOrder: Left --> Right --> Root   45268731
  def postOrder(self, start):
    traversal = ""
    if start:
        traversal += self.postOrder(start.left)
        traversal += self.postOrder(start.right)
        traversal += (str(start.value) + "") 
    return traversal
        
    
  
  
      
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right= Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(tree.print_tree("preOrder"))
print(tree.print_tree("inOrder"))
print(tree.print_tree("postOrder"))




      
        
    