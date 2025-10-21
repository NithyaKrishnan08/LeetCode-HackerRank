# Find a Peak Element II
# https://leetcode.com/problems/find-a-peak-element-ii/description/
# Leetcode: 1901
# Difficulty: Medium

'''
A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

 

Example 1:



Input: mat = [[1,4],[3,2]]
Output: [0,1]
Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.
Example 2:



Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
Output: [1,1]
Explanation: Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.
'''
from typing import List

class Solution:
  def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
    m, n = len(mat), len(mat[0])
    left, right = 0, n - 1

    while left <= right:
      mid = (left + right) // 2

      # Find the row index of the maximum element in the mid column
      max_row = 0
      for i in range(m):
        if mat[i][mid] > mat[max_row][mid]:
          max_row = i

      left_is_bigger = mid - 1 >= 0 and mat[max_row][mid - 1] > mat[max_row][mid]
      right_is_bigger = mid + 1 < n and mat[max_row][mid + 1] > mat[max_row][mid]

      if not left_is_bigger and not right_is_bigger:
        return [max_row, mid]
      elif right_is_bigger:
        left = mid + 1
      else:
        right = mid - 1

    return [-1, -1]
  
if __name__ == "__main__":
  sol = Solution()
  print(sol.findPeakGrid(mat = [[1,4],[3,2]]))  # Output: [0,1]
  print(sol.findPeakGrid(mat = [[10,20,15],[21,30,14],[7,16,32]]))  # Output: [1,1]
