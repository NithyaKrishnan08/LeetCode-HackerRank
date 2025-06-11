# Largest Rectangle in histogram

'''


Code

Testcase

Test Result
Test Result
84. Largest Rectangle in Histogram
Hard

Topics
premium lock icon
Companies
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
'''
from typing import List

class Solution:
  # Brute Force Solution
  def largestRectangleArea1(self, heights: List[int]) -> int:
    def findNextSmallerElement(arr):
      n = len(arr)
      nse_arr = [-1] * n
      stack = []

      for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
          stack.pop()

        nse_arr[i] = n if not stack else stack[-1]

        stack.append(i)

      return nse_arr
    
    def findPreviousSmallerElement(arr):
      n = len(arr)
      pse_arr = [-1] * n
      stack = []

      for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
          stack.pop()

        pse_arr[i] = -1 if not stack else stack[-1]

        stack.append(i)

      return pse_arr
    
    nse_arr = findNextSmallerElement(heights)
    pse_arr = findPreviousSmallerElement(heights)

    max_rectangle = 0

    for i in range(len(heights)):
      width = nse_arr[i] - pse_arr[i] - 1
      area = heights[i] * width
      max_rectangle = max(max_rectangle, area)

    return max_rectangle
  
  # Optimal solution
  # TC: O(N) + O(N)
  # SC: O(N)

  def largestRectangleArea(self, heights: List[int]) -> int:
    n = len(heights)
    max_rectangle = 0
    stack = []

    for i in range(n):
      while stack and heights[stack[-1]] > heights[i]:
        top = stack.pop()
        height = heights[top]
        width = i if not stack else i - stack[-1] - 1
        max_rectangle = max(max_rectangle, height * width)
      stack.append(i)

    while stack:
      top = stack.pop()
      height = heights[top]
      width = n if not stack else n - stack[-1] - 1
      max_rectangle = max(max_rectangle, height * width)

    return max_rectangle

if __name__ == "__main__":
  heights = [2,1,5,6,2,3]
  solution = Solution()
  result = solution.largestRectangleArea(heights)
  print(result)