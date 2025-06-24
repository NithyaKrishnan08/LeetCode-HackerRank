# Detect a cycle in undirected graph using DFS

# TC: O(N + E)
# SC: O(N)
from collections import deque, defaultdict

class Graph:
  def __init__(self):
    self.graph = defaultdict(list)

  def add_edge(self, u , v):
    self.graph[u].append(v)
    self.graph[v].append(u)

  def has_cycle_dfs(self):
    visited = set()
    for node in self.graph:
      if node not in visited:
        if self.dfs(node, -1, visited):
          return True
        
    return False
  
  def dfs(self, node, parent, visited):
    visited.add(node)

    for neightbor in self.graph[node]:
      if neightbor not in visited:
        if self.dfs(neightbor, node, visited):
          return True
      elif neightbor != parent:
        return True
        
    return False
  
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 1)

result = g.has_cycle_dfs()
print("Graph has cycle: ", result)