# Find the City with the smallest number of neighbors at a threshold distance
# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/

'''
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

 

Example 1:



Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2] 
City 1 -> [City 0, City 2, City 3] 
City 2 -> [City 0, City 1, City 3] 
City 3 -> [City 1, City 2] 
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.
Example 2:



Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1] 
City 1 -> [City 0, City 4] 
City 2 -> [City 3, City 4] 
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3] 
The city 0 has 1 neighboring city at a distanceThreshold = 2.
 

Constraints:

2 <= n <= 100
1 <= edges.length <= n * (n - 1) / 2
edges[i].length == 3
0 <= fromi < toi < n
1 <= weighti, distanceThreshold <= 10^4
All pairs (fromi, toi) are distinct.
'''
# Time: O(n³) due to Floyd-Warshall.
# Space: O(n²) for the distance matrix.

from typing import List
from collections import defaultdict
import heapq

class Solution:
  def findTheCityFloyd(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    dist = [[float('inf')] * n for _ in range(n)]
    for u, v, w in edges:
      dist[u][v] = w
      dist[v][u] = w

    for i in range(n):
      dist[i][i] = 0

    for k in range(n):
      for i in range(n):
        for j in range(n):
          if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    count_city = n
    city_no = -1

    for city in range(n):
      count = 0
      for adj_city in range(n):
        if dist[city][adj_city] <= distanceThreshold:
          count += 1

      if count <= count_city:
        count_city = count
        city_no = city

    return city_no
  
  def findTheCityDijkstra(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    graph = defaultdict(list)
    for u, v, w in edges:
      graph[u].append((v, w))
      graph[v].append((u, w))

    def dijkstra(start):
      min_heap = [(0, start)]
      dist = [float('inf')] * n
      dist[start] = 0

      while min_heap:
        curr_dist, node = heapq.heappop(min_heap)

        for neighbor, weight in graph[node]:
          if curr_dist + weight < dist[neighbor]:
            dist[neighbor] = curr_dist + weight
            heapq.heappush(min_heap, (dist[neighbor], neighbor))
      
      return dist

    min_count = float('inf')
    city_no = -1

    for city in range(n):
      distances = dijkstra(city)
      count = sum(1 for d in distances if d <= distanceThreshold and d != 0)

      if count <= min_count:
        min_count = count
        city_no = city

    return city_no
  
if __name__ == "__main__":
  sol = Solution()
  n = 4
  edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
  distanceThreshold = 4

  result = sol.findTheCityFloyd(n, edges, distanceThreshold)
  print(result)

  result = sol.findTheCityDijkstra(n, edges, distanceThreshold)
  print(result)
