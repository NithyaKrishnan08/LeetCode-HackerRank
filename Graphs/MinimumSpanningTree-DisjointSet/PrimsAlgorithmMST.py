# Prim's Algorithm - MST

'''
Problem Statement: Given a weighted, undirected, and connected graph of V vertices and E edges. The task is to find the sum of weights of the edges of the Minimum Spanning Tree.
(Sometimes it may be asked to find the MST as well, where in the MST the edge-informations will be stored in the form {u, v}(u = starting node, v = ending node).)

Example 1:

Input Format: 
V = 5, edges = { {0, 1, 2}, {0, 3, 6}, {1, 2, 3}, {1, 3, 8}, {1, 4, 5}, {4, 2, 7}}


Result: 16
Explanation: 
The minimum spanning tree for the given graph is drawn below:
MST = {(0, 1), (0, 3), (1, 2), (1, 4)}


Example 2:

Input Format: 
V = 5, edges = { {0, 1, 2}, {0, 2, 1}, {1, 2, 1}, {2, 3, 2}, {3, 4, 1}, {4, 2, 2}}
Result: 5
Explanation: 
The minimum spanning tree is drawn below:

MST = {(0, 2), (1, 2), (2, 3), (3, 4)}
'''
# TC: O(E log V)
# SC: O(V + E)

from typing import List
from collections import defaultdict
import heapq

class Solution:
  def spanningTree(self, V: int, edges: List[List[int]]) -> int:
    graph = defaultdict(list)
    for u, v, w in edges:
      graph[u].append((v, w))
      graph[v].append((u, w))

    visited = [0] * V
    min_heap = [(0, 0, -1)] # (distance, node, parent)
    mst_sum = 0
    mst_array = []

    while min_heap:
      current_distance, node, parent = heapq.heappop(min_heap)

      if visited[node]:
        continue
      
      visited[node] = 1
      mst_sum += current_distance
      if parent != -1:
        mst_array.append((parent, node))

      for neighbor, weight in graph[node]:
        if not visited[neighbor]:
          heapq.heappush(min_heap, (weight, neighbor, node))
          
    return mst_sum, mst_array
  
if __name__ == "__main__":
  V = 5
  edges = [ [0, 1, 2], [0, 3, 6], [1, 2, 3], [1, 3, 8], [1, 4, 5], [4, 2, 7] ]
  sol = Solution()
  result = sol.spanningTree(V, edges)
  print(result)
    

