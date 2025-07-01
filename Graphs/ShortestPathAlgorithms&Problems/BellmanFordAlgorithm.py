# Bellman Ford Algorithm
# Application for Directed Graphs
# Works with negative edges and helps to detect negative cycles
# If any graph has path weight < 0, it has negative cycle

# Relax all the edges (N - 1) times sequentially
# Relax of edges -> if dist[u] + wt < dist[v] => dist[v] = dist[u] + wt

# How to detect negative cycles? -> On the Nth iteration, the relaxation will be done and if dist[] arrays gets reduced, negative cycle exists

'''
Given a weighted, directed and connected graph of V vertices and E edges, Find the shortest distance of all the vertices from the source vertex S.

Note: If the Graph contains a negative cycle then return an array consisting of only -1.

Example 1:

Input Format: 
V = 6, 
E = [[3, 2, 6], [5, 3, 1], [0, 1, 5], [1, 5, -3], [1, 2, -2], [3, 4, -2], [2, 4, 3]], 
S = 0


Result: 0 5 3 3 1 2
Explanation: Shortest distance of all nodes from the source node is returned.
'''

from typing import List

class Solution:
  def bellmanFord(self, V: int, edges: List[List[int]], S: int) -> List[int]:
    INF = int(1e8)
    dist = [INF] * V
    dist[S] = 0

    # Step 1: Relax all the edges V-1 times
    for _ in range(V - 1):
      for u, v, wt in edges:
        if dist[u] != INF and dist[u] + wt < dist[v]:
          dist[v] = dist[u] + wt

    # Step 2: Check for negative-weight cycles
    for u, v, wt in edges:
      if dist[u] != INF and dist[u] + wt < dist[v]:
        return -1 # Negative cycle detected
      
    return dist
  
if __name__ == "__main__":
  V = 6
  edges = [
    [3, 2, 6],
    [5, 3, 1],
    [0, 1, 5],
    [1, 5, -3],
    [1, 2, -2],
    [3, 4, -2],
    [2, 4, 3]
  ]
  S = 0

  sol = Solution()
  result = sol.bellmanFord(V, edges, S)
  print(result)

