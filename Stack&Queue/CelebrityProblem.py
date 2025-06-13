# The Celebrity Problem -> Everyone should know him but he knows no one

'''
Given a square matrix mat[][] of size n x n, such that mat[i][j] = 1 means ith person knows jth person, the task is to find the celebrity. A celebrity is a person who is known to all but does not know anyone. Return the index of the celebrity, if there is no celebrity return -1.

Note: Follow 0-based indexing and mat[i][i] will always be 1.

Examples:  

Input: mat[][] = [[1, 1, 0], 
                             [0, 1, 0], 
                             [0, 1, 1]]
Output: 1
Explanation: 0th and 2nd person both know 1. Therefore, 1 is the celebrity.

Input: mat[][] = [[1, 1], 
                            [1, 1]]
Output: -1
Explanation: The two people at the party both know each other. None of them is a celebrity.

Input: mat[][] = [[1]]
Output: 0
'''
# brute force solution
# TC: O(n * n) + O(n)
# SC: O(2N)
def celebrity1(matrix):
  n = len(matrix)
  others_know = [0] * n
  celebrity_knows = [0] * n
  
  for i in range(n):
    for j in range(n):
      if matrix[i][j] == 1:
        others_know[j] += 1
        celebrity_knows[i] += 1

  for i in range(n):
    if others_know[i] == n - 1 and celebrity_knows[i] == 0:
      return i

  return -1

# Optimal solution
# TC: O(2n)
# SC: O(1)
def celebrity(matrix):
  n = len(matrix)
  top = 0
  down = n - 1
  
  while top < down:
    if matrix[top][down] == 1:
      top += 1
    elif matrix[down][top] == 1:
      down -= 1
    else:
      top += 1
      down -= 1


  if top > down:
    return -1

  for i in range(n):
    if matrix[top][i] == 0 and matrix[i][top] == 1:
      return top
    else:
      return -1
    
  return top
  

if __name__ == "__main__":
  mat = [[0, 1, 0],
          [0, 0, 0],
          [0, 1, 0]]
  result = celebrity(mat)
  print(result)


