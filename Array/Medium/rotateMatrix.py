# Rotate Image/ Matrix
# https://leetcode.com/problems/rotate-image/description/
# Difficulty: Medium

'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
'''

from typing import List

def printMatrix(matrix: List[List[int]]) -> None:
  n = len(matrix)
  for i in range(n):
    for j in range(n):
      print(matrix[i][j], end=" ")
    print()

# Brutal solution
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
def rotateMatrix1(matrix: List[List[int]]) -> List[int]:
  n = len(matrix)
  result = [[0 for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      result[j][n-i-1] = matrix[i][j]
  return result

# Optimal solution
# Time Complexity: O(n/2 * n/2)
# Space Complexity: O(1)
def rotateMatrix2(matrix: List[List[int]]) -> None:
  n = len(matrix)
  
  for i in range(n):
    for j in range(i, n):
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
  
  for i in range(n):
    matrix[i].reverse()

if __name__ == "__main__":
  matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

  # print("Brute force solution: ")
  # print("Original matrix: ")
  # printMatrix(matrix)
  # result = rotateMatrix1(matrix)
  # print("\nRotating matrix by 90 degree (clock-wise): ")
  # printMatrix(result)

  print("Optimal solution: ")
  print("Original matrix: ")
  printMatrix(matrix)
  rotateMatrix2(matrix)
  print("\nRotating matrix by 90 degree (clock-wise): ")
  printMatrix(matrix)