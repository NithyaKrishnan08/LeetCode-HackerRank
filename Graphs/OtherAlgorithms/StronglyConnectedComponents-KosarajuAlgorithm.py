# Strongly Connected Algorithm (SCC) - Kosaraju's Algorithm

# 1. Sort all the edges according to the finishing time
# 2. Reverse the edges
# 3. Do a DFS

'''
Problem Statement: Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, Find the number of strongly connected components in the graph.

Pre-requisite: DFS algorithm

Example 1:

Input Format:


Result: 3
Explanation: Three strongly connected components are marked below:

Example 2:

Input Format:


Result: 4
Explanation: Four strongly connected components are marked below:
'''
from collections import defaultdict

class Graph:
  def __init__(self, vertices):
    self.V = vertices
    self.graph = defaultdict(list)

  def add_edge(self, u, v):
    self.graph[u].append(v)

  # Step 1: DFS to fill finishing time
  def dfs_fill_order(self, v, visited, stack):
    visited[v] = True
    for neighbor in self.graph[v]:
      if not visited[neighbor]:
        self.dfs_fill_order(neighbor, visited, stack)
    stack.append(v)

  # Step 2: Transpose the graph
  def get_transpose(self):
    g = Graph(self.V)
    for u in self.graph:
      for v in self.graph[u]:
        g.add_edge(v, u)
    return g
  
  # Standard DFS
  def dfs_util(self, v, visited):
    visited[v] = True
    for neighbor in self.graph[v]:
      if not visited[neighbor]:
        self.dfs_util(neighbor, visited)

  # Step 3: Kosaraju's Algorithm
  def kosaraju_scc_count(self):
    stack = []
    visited = [False] * self.V

    # Fill vertices in stack
    for i in range(self.V):
      if not visited[i]:
        self.dfs_fill_order(i, visited, stack)

    # Transpose the graph
    gr = self.get_transpose()

    # Now process all vertices in order defined by the Stack
    visited = [False] * self.V
    scc_count = 0

    while stack:
      v = stack.pop()
      if not visited[v]:
        gr.dfs_util(v, visited)
        scc_count += 1

    return scc_count

if __name__ == "__main__":
  g1 = Graph(5)
  g1.add_edge(1, 0)
  g1.add_edge(0, 2)
  g1.add_edge(2, 1)
  g1.add_edge(0, 3)
  g1.add_edge(3, 4)
  result = g1.kosaraju_scc_count()
  print(result)
