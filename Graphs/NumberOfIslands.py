# Numebr of Islands
# Leetcode 200
# https://leetcode.com/problems/number-of-islands/

from typing import List
from collections import deque

#  TC: O(M * N)
class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    if not grid:
      return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for i in range(rows):
      for j in range(cols):
        if grid[i][j] == '1':
          count += 1
          queue = deque()
          queue.append((i, j))
          grid[i][j] = '0'

          while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
              nr, nc = r + dr, c + dc
              if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                queue.append((nr, nc))
                grid[nr][nc] = '0'

    return count
  
if __name__ == "__main__":
  grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
  sol = Solution()
  result = sol.numIslands(grid)
  print(result)
