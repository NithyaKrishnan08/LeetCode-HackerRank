# Search a 2D Matrix - I

'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
'''
# To convert 1D coordinate to 2D coordinate: index in 2D coordinate & m -> no. of columns
# Row coordinate = index / m
# Column coordinate = index % m

# Optimal solution
# Time Complexity: O(log2(n*m))
# Space Complexity: O(1)

from typing import List, Optional 

class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    n = len(matrix)
    m = len(matrix[0])

    low = 0
    high = n * m - 1

    while low <= high:
      mid = (low + high) // 2
      row = mid // m
      col = mid % m

      if matrix[row][col] == target:
        return True
      elif (matrix[row][col] < target):
        low = mid + 1
      else:
        high = mid - 1

    return False
  
if __name__ == "__main__":
  matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
  target = 3

  solution = Solution()
  result = solution.searchMatrix(matrix, target)
  if result:
    print(f"{target} is found in matrix")
  else:
    print(f"{target} is not found in matrix")
