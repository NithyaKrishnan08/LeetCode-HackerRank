# Dijkstra's Algorithm using Priority Queue - Undirected Weighted Graph

from typing import List
import heapq
from collections import defaultdict

class Solution:
  def dijkstra(self, edges, V, src):
    # Step 1: Build the adjacency list
    graph = defaultdict(list)
    for u, v, w in edges:
      graph[u].append((v, w))
      graph[v].append((u, w))

    # Step 2: Initialize the distance array and priority queue
    dist = [float('inf')] * V
    dist[src] = 0

    # Step 3: Min-heap to get the minimum distance node
    min_heap = [(0, src)]  # (distance, node)

    while min_heap:
      current_dist, node = heapq.heappop(min_heap)

      # Skip if we already found a better path
      if current_dist > dist[node]:
        continue

      # Step 4: Explore the neighbors
      for neighbor, weight in graph[node]:
        if dist[neighbor] > dist[node] + weight:
          dist[neighbor] = dist[node] + weight
          heapq.heappush(min_heap, (dist[neighbor], neighbor))

    return dist
  
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
  V = 6  # number of vertices
  src = 0
  sol = Solution()
  shortest_distances = sol.dijkstra(edges, V, src)
  print("Shortest distances from source node", src, ":", shortest_distances)