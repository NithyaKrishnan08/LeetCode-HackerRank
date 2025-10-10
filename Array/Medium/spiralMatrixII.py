# Spiral Matrix II
# https://leetcode.com/problems/spiral-matrix-ii/description/
# Difficulty: Medium

'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
'''
from typing import List

# Optimal solution
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
class Solution:
  def generateMatrix(self, n: int) -> List[List[int]]:
    matrix = [[0] * n for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1

    while top <= bottom and left <= right:
      # Left -> Right
      for j in range(left, right + 1):
        matrix[top][j] = num
        num += 1
      top += 1

      # Top -> Bottom
      for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
      right -= 1

      if top <= bottom:
        # Right -> Left
        for j in range(right, left - 1, -1):
          matrix[bottom][j] = num
          num += 1
        bottom -= 1

      if left <= right:
        # Bottom -> Top
        for i in range(bottom, top - 1, -1):
          matrix[i][left] = num
          num += 1
        left += 1
    
    return matrix

if __name__ == "__main__":
  sol = Solution()
  print(sol.generateMatrix(n = 3))