# Making a large island
# https://leetcode.com/problems/making-a-large-island/description/

'''
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.
'''
from typing import List

class DisjointSet:
  def __init__(self, n):
    self.rank = [0] * n
    self.size = [1] * n
    self.parent = [i for i in range(n)]

  def findParent(self, node):
    if node == self.parent[node]:
      return node
    
    # Path Compression
    self.parent[node] = self.findParent(self.parent[node])

    return self.parent[node]

  def unionBySize(self, u, v):
    ultParent_u = self.findParent(u)
    ultParent_v = self.findParent(v)

    if ultParent_u == ultParent_v:
      return
    
    if self.size[ultParent_u] < self.size[ultParent_v]:
      self.parent[ultParent_u] = ultParent_v
      self.size[ultParent_v] += self.size[ultParent_u]
    else:
      self.parent[ultParent_v] = ultParent_u
      self.size[ultParent_u] += self.size[ultParent_v]
  
class Solution:
  def largestIsland(self, grid: List[List[int]]) -> int:
    n = len(grid)
    ds = DisjointSet(n * n)
    directions = [(0,1), (0, -1), (1, 0), (-1, 0)]

    # Step 1: Build Disjoint Set for all 1s
    for r in range(n):
      for c in range(n):
        if grid[r][c] == 1:
          for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
              node_id = r * n + c
              adjNode_id = nr * n + nc
              ds.unionBySize(node_id, adjNode_id)

    max_island = 0

    # Step 2: Try flipping each 0 to 1 and calculate potential island size
    for r in range(n):
      for c in range(n):
        if grid[r][c] == 0:
          components = set()

          for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
              components.add(ds.findParent(nr * n + nc))
        
          potential_size = 1 # For the flipped 0

          for component in components:
            potential_size += ds.size[component]

          max_island = max(max_island, potential_size)

    # Step 3: Handle the case where the entire grid is 1s
    for i in range(n * n):
      if ds.parent[i] == i:
        max_island = max(max_island, ds.size[i])

    return max_island
  
if __name__ == "__main__":
  sol = Solution()
  grid = [[1,1],[1,1]]
  print(sol.largestIsland(grid))
