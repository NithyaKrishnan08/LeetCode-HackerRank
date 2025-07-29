# Minimum Path Sum in Grid
# https://leetcode.com/problems/minimum-path-sum/description/

'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200
'''
from typing import List

class Solution:
  # Recursion
  # TC: 2^(m * n)
  # SC: O(path length) -> O((m-1) + (n-1))
  def minPathSum0_util(self, i, j, grid) -> int:
    # Base cases
    if i == 0 and j == 0:
      return grid[0][0]
    
    if i < 0 or j < 0:
      return int(1e9)
    
    moving_up = grid[i][j] + self.minPathSum0_util(i - 1, j, grid)
    moving_left = grid[i][j] + self.minPathSum0_util(i, j - 1, grid)

    return min(moving_up, moving_left)
  
  def minPathSum0(self, grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    return self.minPathSum0_util(m - 1, n - 1, grid)
  
  # Memoization
  # TC: O(m * n)
  # SC: O(path length) -> O((m-1) + (n-1)) + O(n * m)
  def minPathSum1_util(self, i, j, grid, dp) -> int:
    # Base cases
    if i == 0 and j == 0:
      return grid[0][0]
    
    if i < 0 or j < 0:
      return int(1e9)
    
    if dp[i][j] != -1:
      return dp[i][j]
    
    moving_up = grid[i][j] + self.minPathSum1_util(i - 1, j, grid, dp)
    moving_left = grid[i][j] + self.minPathSum1_util(i, j - 1, grid, dp)

    dp[i][j] = min(moving_up, moving_left)
    return dp[i][j]
  
  def minPathSum1(self, grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    dp = [[-1 for _ in range(n)] for _ in range(m)]

    return self.minPathSum1_util(m - 1, n - 1, grid, dp)
  
  # Tabulation
  # TC: O(m * n)
  # SC: O(path length) -> O((m-1) + (n-1)) + O(n * m)
  def minPathSum2_util(self, m, n, grid, dp) -> int:
    for i in range(m):
      for j in range(n):
        if i == 0 and j == 0:
          dp[i][j] = grid[i][j]
        else:
          moving_up = grid[i][j]
          if i > 0:
            moving_up += dp[i - 1][j]
          else:
            moving_up += int(1e9)
          
          moving_left = grid[i][j]
          if j > 0:
            moving_left += dp[i][j - 1]
          else:
            moving_left += int(1e9)
            
          dp[i][j] = min(moving_up, moving_left)
          
    return dp[m - 1][n - 1]
  
  def minPathSum2(self, grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    dp = [[-1 for _ in range(n)] for _ in range(m)]

    return self.minPathSum2_util(m, n, grid, dp)
  
  # Space Optimization
  # TC: O(m * n)
  # SC: O(n)
  def minPathSum3(self, grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    prev = [0] * n
    
    for i in range(m):
      temp = [0] * n
      for j in range(n):
        if i == 0 and j == 0:
          temp[j] = grid[i][j]
        else:
          moving_up = grid[i][j]     
          if i > 0:
            moving_up += prev[j]
          else:
            moving_up = int(1e9)

          moving_left = grid[i][j]  
          if j > 0:
            moving_left += temp[j - 1]
          else:
            moving_left = int(1e9)

          
          temp[j] = min(moving_up, moving_left)
      
      prev = temp

    return prev[n - 1]
  
if __name__ == "__main__":
  grid = [[1,2,3],[4,5,6]]
  sol = Solution()

  # Recursive
  # result = sol.minPathSum0(grid)
  # print(result)

  # Memoization
  # result = sol.minPathSum1(grid)
  # print(result)

  # Tabulation
  # result = sol.minPathSum2(grid)
  # print(result)

  # Space Optimization
  result = sol.minPathSum3(grid)
  print(result)
