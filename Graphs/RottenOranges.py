# Rotten Oranges
'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

'''
from typing import List
from collections import deque

class Solution:
  def orangesRotting(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    # Initialize the queue with all rotten oranges and count fresh oranges
    for r in range(rows):
      for c in range(cols):
        if grid[r][c] == 2:
          queue.append((r, c))
        elif grid[r][c] == 1:
          fresh += 1

    #  If no fresh oranges initailly, return 0
    if fresh == 0:
      return 0
    
    minutes = 0
    # Directions for 4-directional adjacency -> down, up, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
      size = len(queue)
      for _ in range(size):
        r, c = queue.popleft()
        # Check for all 4 directions
        for dr, dc in directions:
          nr, nc = r + dr, c + dc
          # If new position is within bounds and has fresh oranges
          if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
            grid[nr][nc] = 2
            fresh -= 1
            queue.append((nr, nc))

      # Increment time after processing all rotten oranges at this minute
      if queue:
        minutes += 1

    # If there are still fresh oranges left, return -1
    return minutes if fresh == 0 else -1
  
if __name__ == "__main__":
  grid = [[0,2]]
  solution = Solution()
  result = solution.orangesRotting(grid)
  print(result)