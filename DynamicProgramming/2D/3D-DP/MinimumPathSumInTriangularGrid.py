# Minimum Path Sum in triangular Grid
# https://leetcode.com/problems/triangle/description/
# Fixed starting point and variable ending point

'''
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10
 

Constraints:

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104
'''
from typing import List

class Solution:
  # Recursion
  # TC: 2^(m * n)
  # SC: O(path length) -> O((m-1) + (n-1))
  def minimumTotal0_util(self, i, j, triangle) -> int:
    m = len(triangle)
    # Base cases
    if i == m - 1:
      return triangle[m - 1][j]
    
    moving_down = triangle[i][j] + self.minimumTotal0_util(i + 1, j, triangle)
    moving_down_diagonal = triangle[i][j] + self.minimumTotal0_util(i + 1, j + 1, triangle)

    return min(moving_down, moving_down_diagonal)
  
  def minimumTotal0(self, triangle: List[List[int]]) -> int:
    m = len(triangle)
    return self.minimumTotal0_util(0, 0, triangle)
  
  # Memoization
  # TC: O(n * n)
  # SC: O(path length) -> O((m-1) + (n-1)) + O(n * n)
  def minimumTotal1_util(self, i, j, triangle, dp) -> int:
    m = len(triangle)
    # Base cases
    if i == m - 1:
      return triangle[m - 1][j]
    
    if dp[i][j] != -1:
      return dp[i][j]
    
    moving_down = triangle[i][j] + self.minimumTotal1_util(i + 1, j, triangle, dp)
    moving_down_diagonal = triangle[i][j] + self.minimumTotal1_util(i + 1, j + 1, triangle, dp)

    dp[i][j] = min(moving_down, moving_down_diagonal)
    return dp[i][j]
  
  def minimumTotal1(self, triangle: List[List[int]]) -> int:
    m = len(triangle)
    dp = [[-1 for _ in range(m)] for _ in range(m)]

    return self.minimumTotal1_util(0, 0, triangle, dp)
  
  # Tabulation
  # TC: O(m * m)
  # SC: O(m * m)
  def minimumTotal2_util(self, triangle, dp) -> int:
    m = len(triangle)
    for j in range(m):
      dp[m - 1][j] = triangle[m-1][j]

    for i in range(m - 2, -1, -1):
      for j in range(i  , -1, -1):
        moving_down = triangle[i][j] + dp[i + 1][j]
        moving_down_diagonal = triangle[i][j] + dp[i + 1][j + 1]

        dp[i][j] = min(moving_down, moving_down_diagonal)
    
    return dp[0][0]
  
  def minimumTotal2(self, triangle: List[List[int]]) -> int:
    m = len(triangle)
    dp = [[-1 for _ in range(m)] for _ in range(m)]

    return self.minimumTotal2_util(triangle, dp)
  
  # Space Optimization
  # TC: O(m * n)
  # SC: O(n)
  def minimumTotal3(self, triangle: List[List[int]]) -> int:
    m = len(triangle)

    front = triangle[m - 1][:]
    curr = [0] * m
    
    for i in range(m - 2, -1, -1):
      for j in range(i, -1, -1):
        moving_down = triangle[i][j] + front[j]
        moving_down_diagonal = triangle[i][j] + front[j + 1]

        curr[j] = min(moving_down, moving_down_diagonal)
    
      front = curr[:]

    return front[0]
  
if __name__ == "__main__":
  triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
  sol = Solution()

  # Recursive
  # result = sol.minimumTotal0(triangle)
  # print(result)

  # Memoization
  # result = sol.minimumTotal1(triangle)
  # print(result)

  # Tabulation
  # result = sol.minimumTotal2(triangle)
  # print(result)

  # Space Optimization
  result = sol.minimumTotal3(triangle)
  print(result)
