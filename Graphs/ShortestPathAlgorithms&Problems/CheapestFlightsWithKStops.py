# Cheapest Flights with K Stops
# LeetCode 787
# https://leetcode.com/problems/cheapest-flights-within-k-stops/

'''
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

 

Example 1:


Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
Example 2:


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
Example 3:


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
 

Constraints:

1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 104
There will not be any multiple flights between two cities.
0 <= src, dst, k < n
src != dst
'''

from typing import List
import heapq
from collections import defaultdict
# TC: O(E * log V) — each node and edge can be pushed into the heap.
# SC: O(V * E) — for the adjacency list and the distance array.

class Solution:
  def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    graph = defaultdict(list)
    for u, v, w in flights:
      graph[u].append((v, w))

    min_heap = [(0, src, 0)] # (costs_so_far, current_node, stops_used)
    visited = dict() # (node, stops) -> cost

    while min_heap:
      cost, node, stops = heapq.heappop(min_heap)

      if node == dst:
        return cost
      
      if (node, stops) in visited and visited[(node, stops)] <= cost:
        continue
      visited[(node, stops)] = cost
      
      if stops <= k:
        for neighbor, price in graph[node]:
          new_cost  = cost + price
          heapq.heappush(min_heap, (new_cost, neighbor, stops + 1))

    return -1
  
if __name__ == "__main__":
  n = 3
  flights = [[0,1,100],[1,2,100],[0,2,500]]
  src = 0
  dst = 2
  k = 0

  sol = Solution()
  shortest_distances = sol.findCheapestPrice(n, flights, src, dst, k)
  print("Shortest distances from source node", src, ":", shortest_distances)