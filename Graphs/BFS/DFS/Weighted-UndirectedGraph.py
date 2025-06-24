# Graph Representation - Weighted Undirected Graph

# TC: O(N)
# SC: O(N * N)
from collections import defaultdict

class WeightedGraph:
  def __init__(self):
    self.graph = defaultdict(list)

  def add_edge(self, u, v, w):
    self.graph[u].append((v, w))
    self.graph[v].append((u, w))

  def print_graph(self):
    for node in self.graph:
      print(f"{node} -> {self.graph[node]}")  

g = WeightedGraph()
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 5)
g.add_edge(1, 2, 3)

g.print_graph()