# Floyd Warshall Algorithm

# multisource shortest path
# Detect negative cycles
# go via every vertex

'''
Problem Statement: The problem is to find the shortest distances between every pair of vertices in a given edge-weighted directed graph. The graph is represented as an adjacency matrix of size n*n. Matrix[i][j] denotes the weight of the edge from i to j. If Matrix[i][j]=-1, it means there is no edge from i to j.

Do it in place.

Example 1:

Input Format: 
matrix[][] = { {0, 2, -1, -1},
        {1, 0, 3, -1},{-1, -1, 0, -1},{3, 5, 4, 0} }

Result:
0 2 5 -1 
1 0 3 -1 
-1 -1 0 -1 
3 5 4 0 
Explanation: In this example, the final matrix 
is storing the shortest distances. For example, matrix[i][j] is 
storing the shortest distance from node i to j.
Example 2:

Input Format: 
matrix[][] = {{0,25},
              {-1,0}}


Result:   
0 25  
-1 0﻿
Explanation: In this example, the shortest distance 
is already given (if it exists).
'''
# Time: O(n³)
# Space: O(1) (in-place modification)
from typing import List

class Solution:
  def floydWarshall(self, matrix):
    n = len(matrix)

    # Step 1: Replace -1 with inf (for calculation)
    for i in range(n):
      for j in range(n):
        if matrix[i][j] == -1 and i != j:
          matrix[i][j] = float('inf')
        if i == j:
          matrix[i][j] = 0

    # Step 2: Floyd-Warshall main loop
    for k in range(n):
      for i in range(n):
        for j in range(n):
          if matrix[i][k] != float('inf') and matrix[k][j] != float('inf'):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j]) 
      
    # To detect negative cycle
    for i in range(n):
      if matrix[i][i] < 0:
        print("Negative cycle exists in matrix")

    # Step 3: Convert inf back to -1 for no path
    for i in range(n):
      for j in range(n):
        if matrix[i][j] == float('inf'):
          matrix[i][j] = -1
  
if __name__ == "__main__":
  matrix = [
    [0, 2, -1, -1],
    [1, 0, 3, -1],
    [-1, -1, 0, -1],
    [3, 5, 4, 0]
  ]

  sol = Solution()
  sol.floydWarshall(matrix)
  print(matrix)
