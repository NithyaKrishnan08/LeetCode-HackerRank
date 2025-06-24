# Topological Sorting (BFS) - Kahn's Algorithm

# Linear ordering of vertices such that for every directed edge u -> v, vertex u comes before v in the ordering.
# It is only possible for Directed Acyclic Graphs (DAGs).

#  insert all nodes with Indegree 0 into a queue

# TC: O(V + E)
# SC: O(V)
from typing import List
from collections import deque

class Solution:
  def topoSort(self, graph: List[List[int]]) -> List[int]:
    n = len(graph)
    in_degree = [0] * n

    # Calculate in-degrees of all the vertices
    for u in range(n):
      for v in graph[u]:
        in_degree[v] += 1

    # Queue for vertices with in-degree 0
    queue = deque()
    for i in range(n):
      if in_degree[i] == 0:
        queue.append(i)

    # List to store the topological order
    topological_order = []

    while queue:
      node = queue.popleft()
      topological_order.append(node)

      # Decrease in-degree of all the neighbors
      for neighbor in graph[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
          queue.append(neighbor)

    # If the topological order contains all vertices, return it
    if len(topological_order) == n:
      return topological_order
    else:
      return []
  
if __name__ == "__main__":
  graph = [[1, 2], [3], [3], []]  # Example graph
  sol = Solution()
  print(sol.topoSort(graph))  # Output: [0, 1, 2, 3] or similar valid topological order