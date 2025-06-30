# Shortest Path in Binary Matrix
# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

'''
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
'''
from typing import List
from collections import deque

# TC: O(N^2)
# SC: O(N^2)

class Solution:
  def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])

    source = [0, 0]
    destination = [rows - 1, cols - 1]

    if grid[source[0]][source[1]] != 0 or grid[destination[0]][destination[1]]!= 0:
      return -1

    directions = [(1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1)]

    queue = deque()
    queue.append((source[0], source[1], 1))

    visited = [[False] * cols for _ in range(rows)]
    visited[source[0]][source[1]] = True

    while queue:
      r, c, dist = queue.popleft()
      
      if [r, c] == destination:
        return dist
      
      for dr, dc in directions:
        nr, nc = r + dr, c + dc

        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and not visited[nr][nc]:
          visited[nr][nc] = True
          queue.append((nr, nc, dist + 1))

    return -1

if __name__ == "__main__":
  grid = [[1,0,0],[1,1,0],[1,1,0]]

  sol = Solution()
  print(sol.shortestPathBinaryMatrix(grid))
