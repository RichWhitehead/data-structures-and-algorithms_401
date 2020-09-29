import queue

graph = {
  'A' : ['B' , 'C'],
  'B' : ['D' , 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
  }

check = [] # this will keep track of all nodes
queue  = []

def breadth_first(visited, graph, node):
      check.append(node)
      queue.append(node)

while queue:
      s = queue.pop(0)
      print (s, end = '')

      for neighbor in graph[s]:
        if neighbor not in check:
          check.append (neighbor)
          queue.append(neighbor)
          
# Driver Code
breadth_first (check, graph, 'A')
print()