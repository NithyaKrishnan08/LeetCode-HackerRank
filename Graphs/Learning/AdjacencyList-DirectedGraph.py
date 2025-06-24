# Graph Representation - Directed Graph

# Adjacency List
# TC: O(N)
# SC: O(N + E)
from collections import defaultdict

class Graph:
  def __init__(self):
    self.graph = defaultdict(list)

  def add_edge(self, u , v):
    self.graph[u].append(v)

  def print_graph(self):
    for node in self.graph:
      print(f"{node} -> {self.graph[node]}")

graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

graph.add_edge(1, 3)

graph.print_graph()