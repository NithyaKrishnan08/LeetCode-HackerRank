# Topological Sorting (DFS)

# Linear ordering of vertices such that for every directed edge u -> v, vertex u comes before v in the ordering.
# It is only possible for Directed Acyclic Graphs (DAGs).

# TC: O(V + E)
# SC: O(V)
from typing import List

class Solution:
  def topoSort(self, graph: List[List[int]]) -> List[int]:
    n = len(graph)
    visited = [False] * n
    stack = []

    def dfs(node):
      visited[node] = True
      for neighbor in graph[node]:
        if not visited[neighbor]:
          dfs(neighbor)
      stack.append(node)

    for i in range(n):
      if not visited[i]:
        dfs(i)

    return stack[::-1]
  
if __name__ == "__main__":
  graph = [[1, 2], [3], [3], []]  # Example graph
  sol = Solution()
  print(sol.topoSort(graph))  # Output: [0, 1, 2, 3] or similar valid topological order