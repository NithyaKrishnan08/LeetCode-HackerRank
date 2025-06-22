# Distance of nearest cell having 0
# Note: This question is the same as 1765: https://leetcode.com/problems/map-of-highest-peak/

'''
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
'''
from typing import List
from collections import deque

class Solution:
  def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    rows, cols = len(mat), len(mat[0])
    queue = deque()

    # Initializing the queue with all cells (row, col) having value 0 and mark 1 cells as infinity
    for r in range(rows):
      for c in range(cols):
        if mat[r][c] == 0:
          queue.append((r, c))
        else:
          mat[r][c] = float('inf')

    # Directions for moving up, down, left, right
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # BFS Traversal
    while queue:
      r, c = queue.popleft()
      for dr, dc in directions:
        nr, nc = r + dr, c + dc
        # We are checking if the new cell is within bounds and if we can update the distance
        if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] > mat[r][c] + 1:
          mat[nr][nc] = mat[r][c] + 1
          queue.append((nr, nc))

    return mat
  
if __name__ == "__main__":
  sol = Solution()
  mat = [[0,0,0],[0,1,0],[1,1,1]]
  result = sol.updateMatrix(mat)
  print(result)
