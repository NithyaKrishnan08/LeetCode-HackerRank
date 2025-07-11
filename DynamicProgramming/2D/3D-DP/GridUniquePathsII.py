# Grid Unique Paths
# https://leetcode.com/problems/unique-paths/description/

'''
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
 

Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
'''
from typing import List

class Solution:
  # Recursion
  # TC: 2^(m * n)
  # SC: O(path length) -> O((m-1) + (n-1))
  def uniquePathsWithObstacles0_util(self, i, j, obstacleGrid) -> int:

    # Base cases
    if i < 0 or j < 0 or obstacleGrid[i][j] == 1:
      return 0
    
    if i == 0 and j == 0:
      return 1
    
    moving_up = self.uniquePathsWithObstacles0_util(i - 1, j, obstacleGrid)
    moving_left = self.uniquePathsWithObstacles0_util(i, j - 1, obstacleGrid)

    return moving_up + moving_left
  
  def uniquePathsWithObstacles0(self, obstacleGrid: List[List[int]]) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    return self.uniquePathsWithObstacles0_util(m - 1, n - 1, obstacleGrid)
  
  # Memoization
  # TC: O(m * n)
  # SC: O(path length) -> O((m-1) + (n-1)) + O(n * m)
  def uniquePathsWithObstacles1_util(self, i, j, obstacleGrid, dp) -> int:

    # Base cases
    if i < 0 or j < 0 or obstacleGrid[i][j] == 1:
      return 0
    
    if i == 0 and j == 0:
      return 1
    
    if dp[i][j] != -1:
      return dp[i][j]
    
    moving_up = self.uniquePathsWithObstacles1_util(i - 1, j, obstacleGrid, dp)
    moving_left = self.uniquePathsWithObstacles1_util(i, j - 1, obstacleGrid, dp)

    dp[i][j] = moving_up + moving_left
    return dp[i][j]
  
  def uniquePathsWithObstacles1(self, obstacleGrid: List[List[int]]) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = [[-1 for _ in range(n)] for _ in range(m)]
  
    return self.uniquePathsWithObstacles1_util(m -1, n - 1, obstacleGrid, dp)
  
  # Tabulation
  # TC: O(m * n)
  # SC: O(m * n)
  def uniquePathsWithObstacles2_util(self, m, n, obstacleGrid, dp) -> int:
    for i in range(m):
      for j in range(n):
        if i > 0 and j > 0 and obstacleGrid[i][j] == 1:
          dp[i][j] = 0
          continue
        if i == 0 and j == 0:
          dp[i][j] = 1
          continue
        moving_up, moving_left = 0, 0
        if i > 0:
          moving_up = dp[i - 1][j]
        if j > 0:
          moving_left = dp[i][j - 1]
        dp[i][j] = moving_up + moving_left
          
    return dp[m - 1][n - 1]
  
  def uniquePathsWithObstacles2(self, obstacleGrid: List[List[int]]) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = [[-1 for _ in range(n)] for _ in range(m)]
  
    return self.uniquePathsWithObstacles2_util(m, n, obstacleGrid, dp)
  
if __name__ == "__main__":
  obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
  sol = Solution()

  # Recursive
  # result = sol.uniquePathsWithObstacles0(obstacleGrid)
  # print(result)

  # Memoization
  # result = sol.uniquePathsWithObstacles1(obstacleGrid)
  # print(result)

  # Tabulation
  result = sol.uniquePathsWithObstacles2(obstacleGrid)
  print(result)
