# Print Shortest Path

import heapq
from collections import defaultdict

class Solution:
  def printShortestPath(self, edges, V, src, target):
    graph = defaultdict(list)
    for u, v, w in edges:
      graph[u].append((v, w))
      graph[u].append((v, w))

    dist = [float('inf')] * V
    parent = [-1] * V

    dist[src] = 0
    min_heap = [(0, src)]

    while min_heap:
      current_dist, node = heapq.heappop(min_heap)

      if current_dist > dist[node]:
        continue

      for neighbor, weight in graph[node]:
        new_dist = dist[node] + weight
        if dist[neighbor] > new_dist:
          dist[neighbor] = new_dist
          parent[neighbor] = node
          heapq.heappush(min_heap, (dist[neighbor], neighbor))

    # Reconstruct path from src to target
    if dist[target] == float('inf'):
      return []
    
    path = []
    current = target
    while current != -1:
      path.append(current)
      current = parent[current]

    return path[::-1]
  
if __name__ == "__main__":
  edges = [
      (0, 1, 2),
      (0, 4, 1),
      (4, 5, 4),
      (4, 2, 2),
      (1, 2, 3),
      (2, 3, 6),
      (5, 3, 1)
  ]
  V = 6
  src = 0
  target = 3

  sol = Solution()
  path = sol.printShortestPath(edges, V, src, target)
  print(path)