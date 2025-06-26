# Shortest path in undirected graph with unit weights

'''
You are given an adjacency list, adj of Undirected Graph having unit weight of the edges, find the shortest path from src to all the vertex and if it is unreachable to reach any vertex, then return -1 for that vertex.

Examples :

Input: adj[][] = [[1, 3], [0, 2], [1, 6], [0, 4], [3, 5], [4, 6], [2, 5, 7, 8], [6, 8], [7, 6]], src=0
Output: [0, 1, 2, 1, 2, 3, 3, 4, 4]
 
Input: adj[][]= [[3], [3], [], [0, 1]], src=3
Output: [1, 1, -1, 0]

Input: adj[][]= [[], [], [], [4], [3], [], []], src=1
Output: [-1, 0, -1, -1, -1, -1, -1] 
Constraint:
1<=adj.size()<=104
0<=edges<=adj.size()-1
'''
from collections import deque
from typing import List

# TC: O(N + E)
# SC: O(N + E)
class Solution:
  def shortestPath(adj: List[List[int]], src: int) -> List[int]:
    n = len(adj)
    distance_from_src = [-1] * n
    distance_from_src[src] = 0

    queue = deque()
    queue.append(src)

    while queue:
      node = queue.popleft()
      for neighbor in adj[node]:
        if distance_from_src[neighbor] == -1:
          distance_from_src[neighbor] = distance_from_src[node] + 1
          queue.append(neighbor)
          
    return distance_from_src

if __name__ == "__main__":
  adj = [[1, 3], [0, 2], [1, 6], [0, 4], [3, 5], [4, 6], [2, 5, 7, 8], [6, 8], [7, 6]]
  src = 0
  print(Solution.shortestPath(adj, src))
