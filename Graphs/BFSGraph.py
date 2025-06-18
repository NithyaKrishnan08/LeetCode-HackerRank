# Breadth First Search (BFS) implementation for a graph
# TC: O(N + E)
from collections import deque, defaultdict

class Graph:
  def __init__(self):
    self.graph = defaultdict(list)

  def add_edge(self,  u, v):
    self.graph[u].append(v)

  def bfs(self, start):
    visited = set()
    queue = deque()
    bfs_elements = []

    visited.add(start)
    queue.append(start)

    while queue:
      node = queue.popleft()
      bfs_elements.append(node)
      for neighbor in self.graph[node]:
        if neighbor not in visited:
          visited.add(neighbor)
          queue.append(neighbor)

    return bfs_elements
  
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

result = g.bfs(2)
print("BFS starting from node 2:", result)
