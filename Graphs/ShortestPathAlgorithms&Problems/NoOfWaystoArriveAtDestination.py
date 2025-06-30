# Number of ways to arrive at destination
# Leetcode  #1976 - https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/description/

'''
You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.

You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.

Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 109 + 7.

 

Example 1:


Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
Output: 4
Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
The four ways to get there in 7 minutes are:
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6
Example 2:

Input: n = 2, roads = [[1,0,10]]
Output: 1
Explanation: There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.
 

Constraints:

1 <= n <= 200
n - 1 <= roads.length <= n * (n - 1) / 2
roads[i].length == 3
0 <= ui, vi <= n - 1
1 <= timei <= 109
ui != vi
There is at most one road connecting any two intersections.
You can reach any intersection from any other intersection.
'''
# TC: O(E log V) — each node and edge can be pushed into the heap.
# SC: O(V + E) — for the adjacency list and the distance array.
from typing import List
from collections import defaultdict
import heapq

class Solution:
  def countPaths(self, n: int, roads: List[List[int]]) -> int:
    # Generate graph
    graph = defaultdict(list)
    for u, v, w in roads:
      graph[u].append((v, w))
      graph[v].append((u, w))

    time_array = [float('inf')] * n
    time_array[0] = 0

    ways_array = [0] * n
    ways_array[0] = 1

    mod = 10**9 + 7

    min_heap = [(0, 0)]

    while min_heap:
      current_time, node = heapq.heappop(min_heap)
      
      for neighbor, weight in graph[node]:
        new_time = current_time + weight
        if new_time < time_array[neighbor]:
          time_array[neighbor] = new_time
          heapq.heappush(min_heap, (time_array[neighbor], neighbor))
          ways_array[neighbor] = ways_array[node]
        elif new_time == time_array[neighbor]:
          ways_array[neighbor] = (ways_array[neighbor] + ways_array[node]) % mod

    return ways_array[n - 1] % mod
  
if __name__ == "__main__":
  n = 7
  roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]

  sol = Solution()
  result = sol.countPaths(n, roads)
  print(result)