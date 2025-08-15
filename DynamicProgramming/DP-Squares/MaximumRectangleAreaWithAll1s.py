# Maximum Rectangle Area with all 1's
# https://leetcode.com/problems/maximal-rectangle/description/
# LeetCode Problem 85

'''
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1
 

Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
'''
from typing import List

class Solution:
  def maximalRectangle(self, matrix: List[List[str]]) -> int:
    if not matrix:
      return 0
    
    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * (cols + 1)
    max_area = 0

    for row in matrix:
      for j in range(cols):
        heights[j] = heights[j] + 1 if row[j] == '1' else 0

      stack = []
      for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
          height = heights[stack.pop()]
          width = i if not stack else i - stack[-1] - 1
          max_area = max(max_area, height * width)

        stack.append(i)

    return max_area
  
if __name__ == '__main__':
  sol = Solution()
  print(sol.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])) # Output: 6
  print(sol.maximalRectangle([["0"]])) # Output: 0
  print(sol.maximalRectangle([["1"]])) # Output: 1

        