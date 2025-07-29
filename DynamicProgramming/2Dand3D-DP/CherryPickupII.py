# Cherry Pickup II
# Problem: https://leetcode.com/problems/cherry-pickup-ii/

# Also, Choclate Pickup in code 360

'''
You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

You have two robots that can collect cherries for you:

Robot #1 is located at the top-left corner (0, 0), and
Robot #2 is located at the top-right corner (0, cols - 1).
Return the maximum number of cherries collection using both robots by following the rules below:

From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
When both robots stay in the same cell, only one takes the cherries.
Both robots cannot move outside of the grid at any moment.
Both robots should reach the bottom row in grid.

Example 1:
Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
Output: 24
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
Total of cherries: 12 + 12 = 24.

Example 2:
Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
Output: 28
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
Total of cherries: 17 + 11 = 28.

Constraints:

rows == grid.length
cols == grid[i].length
2 <= rows, cols <= 70
0 <= grid[i][j] <= 100
'''
# Step 1: Express everything in terms of (i1, j1) and (i2, j2)
# Step 2: Explore all the possible moves for both robots
# Step 3: Maximum sum of cherries collected by both robots

from typing import List
from functools import lru_cache

class Solution:
  # Recursive method
  # TC: (3^n * 3^n) -> exponential
  # SC: O(path length) -> O((m-1) + (n-1) + (n-1))
  # Note: This is not efficient for larger grids,
  #       but it helps to understand the problem and the recursive structure.
  def cherryPickup0_util(self, i, j1, j2, grid):
    m = len(grid)
    n = len(grid[0])

    if j1 < 0 or j1 >= n or j2 < 0 or j2 >= n:
      return -1e9
    
    if i == m - 1:
      if j1 == j2:
        return grid[i][j1]
      else:
        return grid[i][j1] + grid[i][j2]
    
    # Explore all paths of both robots
    max_cherries = -1e9
    for dj1 in [-1, 0, 1]:
      for dj2 in [-1, 0, 1]:
        if j1 == j2:
          max_cherries = max(max_cherries, grid[i][j1] + self.cherryPickup0_util(i + 1, j1 + dj1, j2 + dj2, grid))
        else:
          max_cherries = max(max_cherries, grid[i][j1] + grid[i][j2] + self.cherryPickup0_util(i + 1, j1 + dj1, j2 + dj2, grid))

    return max_cherries
  
  def cherryPickup0(self, grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    return self.cherryPickup0_util(0, 0, n - 1, grid)
  
  # Memoization method
  # TC: O(m * n^2 * 9) -> O(m * n^2)
  # SC: O(m * n^2)
  
  def cherryPickup1(self, grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    # Create a 3D DP table initialized to -1 (uncomputed state)
    dp = [[[ -1 for _ in range(n)] for _ in range(n)] for _ in range(m)]

    def dfs(i, j1, j2):
      # out of bounds for either robots
      if j1 < 0 or j1 >= n or j2 < 0 or j2 >= n:
        return float('-inf')
      
      if i == m - 1:
        if j1 == j2:
          return grid[i][j1]
        else:
          return grid[i][j1] + grid[i][j2]
      
      # Check if already computed
      if dp[i][j1][j2] != -1:
        return dp[i][j1][j2]
      
      # Explore all paths of both robots
      max_cherries = float('-inf')
      for dj1 in [-1, 0, 1]:
        for dj2 in [-1, 0, 1]:
          new_j1 = j1 + dj1
          new_j2 = j2 + dj2
          if j1 == j2:
            value = grid[i][j1]
          else:
            value = grid[i][j1] + grid[i][j2]
          
          value += dfs(i + 1, new_j1, new_j2)
          max_cherries = max(max_cherries, value)
      
      # Store the result in the DP table
      dp[i][j1][j2] = max_cherries
      return max_cherries
    
    return dfs(0, 0, n - 1)
  
if __name__ == "__main__":
  grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
  sol = Solution()

  # Recursion
  # result = sol.cherryPickup0(grid)
  # print(result)

  # Memoization
  result = sol.cherryPickup1(grid)
  print(result)

  # Tabulation
  # result = sol.getMaxPathSum2(matrix)
  # print(result)

  # Space Optimization
  # result = sol.getMaxPathSum3(matrix)
  # print(result)