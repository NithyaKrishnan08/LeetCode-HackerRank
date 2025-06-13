# Maximal Rectangle

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
'''
from typing import List

class Solution:
  def maximalRectangle(self, matrix: List[List[str]]) -> int:
    if not matrix:
      return 0
    
    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * cols
    max_area = 0

    def largestRectangleArea(heights: List[int]) -> int:
      stack = []
      max_area = 0
      n = len(heights)

      for i in range(n):
        while stack and heights[stack[-1]] > heights[i]:
          height = heights[stack.pop()]
          width = i if not stack else i - stack[-1] - 1
          max_area = max(max_area, height * width)
        stack.append(i)

      while stack:
        height = heights[stack.pop()]
        width = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, height * width)

      return max_area
    
    for row in matrix:
      for i in range(cols):
        # Building the histogram
        heights[i] = heights[i] + 1 if row[i] == '1' else 0
      
      max_area = max(max_area, largestRectangleArea(heights))

    return max_area
  
if __name__ == "__main__":
  matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
  solution = Solution()
  result = solution.maximalRectangle(matrix)
  print(result)