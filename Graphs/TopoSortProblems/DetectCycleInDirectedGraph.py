# Detect a cycle in a directed graph using Kahn's algorithm (BFS)

from typing import List
from collections import deque

class Solution:
  def hasCycle(self, graph: List[List[int]]) -> bool:
    n = len(graph)
    in_degree = [0] * n

    # Calculate in-degrees of all the vertices
    for u in range(n):
      for v in graph[u]:
        in_degree[v] += 1

    # Queue for vertices with in-degree  0
    queue = deque()
    for i in range(n):
      if in_degree[i] == 0:
        queue.append(i)

    # Count of visited vertices
    visited_count = 0
# Detect a cycle in a directed graph using Kahn's algorithm (BFS)

from typing import List
from collections import deque

class Solution:
  def hasCycle(self, graph: List[List[int]]) -> bool:
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

    # Count of visited vertices
    visited_count = 0

    while queue:
      node = queue.popleft()
      visited_count += 1

      for neighbor in graph[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
          queue.append(neighbor)

    # If the visited_count != n, then there is a cycle
    return visited_count != n
  
if __name__ == "__main__":
  graph = [[1, 2], [3], [3], []]  # Example graph
  sol = Solution()
  print(sol.hasCycle(graph))