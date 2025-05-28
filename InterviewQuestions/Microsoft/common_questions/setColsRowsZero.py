'''
Problem Statement: Given a two-dimensional array, if any element within is zero, make its whole row and column zero. Consider the matrix below.

Given matrix
There are two zeros in the input matrix at positions (1,1) and (2,3). The output of this should be a matrix in which the first and second rows become zero and the first and third columns become zero. Below is the expected output matrix.


'''

def setColumnsRowsZero(matrix):
  n = len(matrix)
  m = len(matrix[0])

  row_array = [0] * n
  col_array = [0] * m

  for i in range(n):
    for j in range(m):
      if matrix[i][j] == 0:
        row_array[i] = 1
        col_array[j] = 1

  for i in range(n):
    for j in range(m):
      if row_array[i] == 1 or col_array[j] == 1:
        matrix[i][j] = 0

  return matrix

if __name__ == "__main__":
  matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

  result = setColumnsRowsZero(matrix)
  print(result)