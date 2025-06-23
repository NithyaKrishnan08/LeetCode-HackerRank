# Number of Enclaves 
# Leetcode - 1020
# https://leetcode.com/problems/number-of-enclaves/

from typing import List
from collections import deque

class Solution:
  # DFS method
  def numEnclavesDFS(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
      if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
        return
      grid[r][c] = 0  # Mark the cell as visited
      # Explore all the four directions
      dfs(r + 1, c)
      dfs(r - 1, c)
      dfs(r, c + 1)
      dfs(r, c - 1)

    # Step 1: Start DFS from the border cells and fill them with 0
    # check the first and last col
    for i in range(rows):
      if grid[i][0] == 1:
        dfs(i, 0)
      if grid[i][cols - 1] == 1:
        dfs(i, cols - 1)
    # check the first and last row
    for j in range(cols):
      if grid[0][j] == 1:
        dfs(0, j)
      if grid[rows - 1][j] == 1:
        dfs(rows - 1, j)

    # Step 2: Count the remaining 1s in the grid
    count = 0
    for i in range(rows):
      for j in range(cols):
        if grid[i][j] == 1:
          count += 1

    return count
  
  # BFS method
  def numEnclavesBFS(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue = deque()

    # Add boundry land into the queue
    # Checking the first and last columns
    for i in range(rows):
      if grid[i][0] == 1:
        queue.append((i, 0))
      if grid[i][cols - 1] == 1:
        queue.append((i, cols - 1))
    # check the first and last row
    for j in range(cols):
      if grid[0][j] == 1:
        queue.append((0, j))
      if grid[rows - 1][j] == 1:
        queue.append((rows - 1, j))

    # Directions for moving up, down, left and right
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    # Perform BFS to mark all reachable land cells from the boundry
    while queue:
      r, c = queue.popleft()
      if grid[r][c] != 1:
        continue
      grid[r][c] = 0
      for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
          queue.append((nr, nc))

    # Count the remaining 1s in the grid
    count = 0
    for i in range(rows):
      for j in range(cols):
        if grid[i][j] == 1:
          count += 1

    return count
  
if __name__ == "__main__":
  board = grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
  sol = Solution()
  print(sol.numEnclavesDFS(board))

  board = grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
  print(sol.numEnclavesBFS(board))