'''
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
from typing import List

# Optimal solution
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
def spiralOrder(matrix: List[List[int]]) -> List[int]:
  m = len(matrix)
  n = len(matrix[0])
  top = 0
  bottom = m - 1
  left = 0
  right = n - 1
  result = []

  while top <= bottom and left <= right:
    # Left -> Right
    for k in range(left, right + 1):
      result.append(matrix[top][k])
    top += 1

    # Top -> Bottom
    for k in range(top, bottom + 1):
      result.append(matrix[k][right])
    right -= 1

    if top <= bottom:
      # Right -> Left
      for k in range(right, left - 1, -1):
        result.append(matrix[bottom][k])
      bottom -= 1

    if left <= right:
      # Bottom -> Top
      for k in range(bottom, top - 1, -1):
        result.append(matrix[k][left])
      left += 1
  
  return result

if __name__ == "__main__":
  matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

  print("Optimal solution: ")
  result = spiralOrder(matrix)
  print(result)