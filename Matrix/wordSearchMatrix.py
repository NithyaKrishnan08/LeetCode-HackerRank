'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
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