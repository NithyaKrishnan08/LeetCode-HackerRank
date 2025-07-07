# Number of Islands II

'''
Problem Statement: You are given an n, m which means the row and column of the 2D matrix, and an array of size k denoting the number of operations. Matrix elements are 0 if there is water or 1 if there is land. Originally, the 2D matrix is all 0 which means there is no land in the matrix. The array has k operator(s) and each operator has two integers A[i][0], A[i][1] means that you can change the cell matrix[A[i][0]][A[i][1]] from sea to island. Return how many islands are there in the matrix after each operation. You need to return an array of size k.

Note: An island means a group of 1s such that they share a common side.

Pre-requisite: Disjoint Set data structure

Example 1:

Input Format: n = 4 m = 5 k = 4 A = {{1,1},{0,1},{3,3},{3,4}} Output: 1 1 2 2 Explanation: The following illustration is the representation of the operation:

Example 2:

Input Format: n = 4 m = 5 k = 12 A = {{0,0},{0,0},{1,1},{1,0},{0,1},{0,3},{1,3},{0,4}, {3,2}, {2,2},{1,2}, {0,2}} Output: 1 1 2 1 1 2 2 2 3 3 1 1 Explanation: If we follow the process like in example 1, we will get the above result.

'''
from typing import List

class DisjointSet:
  def __init__(self, n):
    self.rank = [0] * (n + 1)
    self.size = [0] * (n + 1)
    self.parent = [i for i in range(n + 1)]

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

    return True

class Solution:
  def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
    ds = DisjointSet(m * n)
    grid = [[0] * n for _ in range(m)]
    count = 0
    result = []
    directions = [(0,1), (0, -1), (1, 0), (-1, 0)]

    for r, c in positions:
      if grid[r][c] == 1:
        result.append(count)
        continue

      grid[r][c] = 1
      count += 1
      curr_id = r * n + c

      for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
          neighbor_id = nr * n + nc
          if ds.unionBySize(curr_id, neighbor_id):
            count -= 1

      result.append(count)

    return result
  
if __name__ == "__main__":
  sol = Solution()
  m, n = 3, 3
  positions = [[0,0], [0,1], [1,2], [2,1], [1,1]]
  print(sol.numIslands2(m, n, positions)) 