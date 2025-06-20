# Depth First Search (DFS) implementation for a graph
# TC: O(N) + O(2 * E)
# SC: O(N) + O(N) + O(N) ~ O(N)
from collections import defaultdict

class Graph:
  def __init__(self):
    self.graph = defaultdict(list)

  def add_edge(self,  u, v):
    self.graph[u].append(v)

  def dfs_util(self, node, visited, dfs_elements):
    visited.add(node)
    dfs_elements.append(node)

    for neighbor in self.graph[node]:
      if neighbor not in visited:
        self.dfs_util(neighbor, visited, dfs_elements)
      
  def dfs(self, start):
    visited = set()
    dfs_elements = []
    self.dfs_util(start, visited, dfs_elements)
    return dfs_elements
  
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

result = g.dfs(2)
print("DFS starting from node 2:", result)
