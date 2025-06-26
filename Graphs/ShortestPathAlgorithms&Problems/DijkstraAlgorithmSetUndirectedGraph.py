# Dijkstra's Algorithm using Set - Undirected Weighted Graph

from typing import List
import heapq
from collections import defaultdict

# TC: O(V^2) — each node and edge can be pushed into the heap.
# SC: O(V + E) — for the adjacency list and the distance array.
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

    # Step 3: Set
    s = set()
    s.add((0, src))

    while s:
      current_dist, node = min(s)
      s.remove((current_dist, node))

      # Step 4: Explore the neighbors
      for neighbor, weight in graph[node]:
        new_dist = dist[node] + weight
        if dist[neighbor] > new_dist:
          if (dist[neighbor], neighbor) in s:
            s.remove((dist[neighbor], neighbor))
          dist[neighbor] = new_dist
          s.add((dist[neighbor], neighbor))

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