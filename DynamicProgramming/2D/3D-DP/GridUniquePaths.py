# Grid Unique Paths
# https://leetcode.com/problems/unique-paths/description/

'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100
'''
from typing import List

class Solution:
  # Recursion
  # TC: 2^(m * n)
  # SC: O(path length) -> O((m-1) + (n-1))
  def uniquePaths0(self, m: int, n: int) -> int:
    # Base cases
    if m == 0 and n == 0:
      return 1
    
    if m < 0 or n < 0:
      return 0
    
    moving_up = self.uniquePaths0(m - 1, n)
    moving_left = self.uniquePaths0(m, n - 1)

    return moving_up + moving_left
  
  # Memoization
  # TC: O(m * n)
  # SC: O(path length) -> O((m-1) + (n-1)) + O(n * m)
  def uniquePaths1_util(self, m: int, n: int, dp) -> int:
    # Base cases
    if m == 0 and n == 0:
      return 1
    
    if m < 0 or n < 0:
      return 0
    
    if dp[m][n] != -1:
      return dp[m][n]
    
    moving_up = self.uniquePaths1_util(m - 1, n, dp)
    moving_left = self.uniquePaths1_util(m, n - 1, dp)
    dp[m][n] = moving_up + moving_left

    return dp[m][n]
  
  def uniquePaths1(self, m: int, n: int) -> int:
    dp = [[-1 for j in range(n)] for i in range(m)]
    return self.uniquePaths1_util(m - 1, n - 1, dp)
  
  # Tabulation
  # TC: O(m * n)
  # SC: O(m * n)
  def uniquePaths2_util(self, m: int, n: int, dp) -> int:
    # Base cases
    dp[0][0] = 1
    
    if m < 0 or n < 0:
      return 0
    
    for i in range(m):
      for j in range(n):
        if i == 0 and j == 0:
          dp[i][j] = 1
        else:
          moving_up, moving_left = 0, 0
          if i > 0:
            moving_up = dp[i - 1][j]
          if j > 0:
            moving_left = dp[i][j - 1]
          dp[i][j] = moving_up + moving_left

    return dp[m - 1][n - 1]
  
  def uniquePaths2(self, m: int, n: int) -> int:
    dp = [[-1 for j in range(n)] for i in range(m)]
    return self.uniquePaths2_util(m, n, dp)
  
  # Space Optimization
  # TC: O(m * n)
  # SC: O(n)
  def uniquePaths3(self, m: int, n: int) -> int:
    prev = [0] * n
    
    for i in range(m):
      temp = [0] * n
      for j in range(n):
        if i == 0 and j == 0:
          temp[j] = 1
          continue
        
        moving_up, moving_left = 0, 0
          
        if i > 0:
          moving_up = prev[j]
        if j > 0:
          moving_left = temp[j - 1]
        
        temp[j] = moving_up + moving_left
      
      prev = temp

    return prev[n - 1]
  
if __name__ == "__main__":
  m = 3
  n = 7
  sol = Solution()

  # Recursive
  # result = sol.uniquePaths0(m - 1, n - 1)
  # print(result)

  # Memoization
  # result = sol.uniquePaths1(m, n)
  # print(result)

  # Tabulation
  # result = sol.uniquePaths2(m, n)
  # print(result)

  # Space Optimization
  result = sol.uniquePaths3(m, n)
  print(result)