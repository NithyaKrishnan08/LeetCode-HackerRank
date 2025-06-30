# Network Delay Time

'''
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
 

Constraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
'''
from typing import List
from collections import defaultdict
import heapq

# TC: O(E log V) — each node and edge can be pushed into the heap.
# SC: O(V + E) — for the adjacency list and the distance array.
class Solution:
  def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    # Step 1: Building adjacency list
    graph = defaultdict(list)
    for u, v, w in times:
      graph[u].append((v, w))

    # Step 2: Initialize visited array
    visited = set()
    min_time = 0

    # Step 3: Min-heap to get the minimum time node
    min_heap = [(0, k)]  # (time, node)

    while min_heap:
      current_time, node = heapq.heappop(min_heap)
      
      if node in visited:
        continue

      visited.add(node)
      min_time = max(min_time, current_time)

      for neighbor, weight in graph[node]:
        if neighbor not in visited:
          heapq.heappush(min_heap, (current_time + weight, neighbor))
          
    return min_time if len(visited) == n else -1
  
if __name__ == "__main__":
  times = [[1,2,1]]
  n = 2
  k = 2

  sol = Solution()
  result = sol.networkDelayTime(times, n, k)
  print(result)