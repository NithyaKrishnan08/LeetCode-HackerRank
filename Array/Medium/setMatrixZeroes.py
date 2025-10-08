# Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/description/
# Difficulty: Medium

'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''

from typing import List

def markRow(i, matrix: List[List[int]]) -> None:
  m = len(matrix[0])
  for j in range(m):
    if matrix[i][j] != 0:
      matrix[i][j] = float('-inf')

def markColumn(j, matrix: List[List[int]]) -> None:
  n = len(matrix)
  for i in range(n):
    if matrix[i][j] != 0:
      matrix[i][j] = float('-inf')

#  Brute force solution
# Time Complexity: O(N^3)
def setZeroes1(matrix: List[List[int]]) -> None:
  n = len(matrix)
  m = len(matrix[0])
  for i in range(n): # O(n*m)
    for j in range(m):
      if matrix[i][j] == 0:
        markRow(i, matrix) # O(n)
        markColumn(j, matrix) # O(m)

  for i in range(n): # O(n*m)
    for j in range(m):
      if matrix[i][j] == float('-inf'):
        matrix[i][j] = 0

#  Better solution
# Time Complexity: O(2 * n * m)
#  SPace Complexity: O(m) + O(n)
def setZeroes2(matrix: List[List[int]]) -> None:
  n = len(matrix)
  m = len(matrix[0])

  row_array = [0] * n
  col_array = [0] * m

  for i in range(n): # O(n*m)
    for j in range(m):
      if matrix[i][j] == 0:
        row_array[i] = 1
        col_array[j] = 1

  for i in range(n): # O(n*m)
    for j in range(m):
      if (row_array[i] == 1 or col_array[j] == 1):
        matrix[i][j] = 0

def printMatrix(matrix: List[List[int]]) -> None:
  n = len(matrix)
  m = len(matrix[0])
  for i in range(n):
    for j in range(m):
      print(matrix[i][j], end=" ")
    print("\n")

if __name__ == "__main__":
  matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
  # print("Brute force solution: ")
  # print("Before setting zeroes: ")
  # printMatrix(matrix)
  # setZeroes1(matrix)
  # print("\nAfter setting zeroes: ")
  # printMatrix(matrix)

  print("Better solution: ")
  print("Before setting zeroes: ")
  printMatrix(matrix)
  setZeroes2(matrix)
  print("\nAfter setting zeroes: ")
  printMatrix(matrix)