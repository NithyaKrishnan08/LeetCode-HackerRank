# Rat in a Maze
# Difficulty: Hard

'''
Given a square binary matrix mat[][] representing a maze. A rat starts at the top-left corner (0,0) and needs to reach the bottom-right corner (n-1, n-1). The rat can move in four directions: Up (U), Down (D), Left (L), Right (R).
Find all possible paths from (0, 0) to (n-1, n-1). If multiple paths exist, return them in lexicographically sorted order otherwise If no path exists, return empty list.

Note:

A rat cannot visit the same cell more than once in a path.
1 represents an open cell (rat can visit), and 0 represents a blocked cell (rat cannot visit).
Example:

Input: mat[][] = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
Output: ["DDRDRR", "DRDDRR"]
Explanation: The possible paths are: DDRDRR, DRDDRR 

'''

from typing import List

class Solution:
  def findPath(self, mat):
    n = len(mat)
    result = []

    # If start or end is blocked -> no path
    if mat[0][0] == 0 or mat[n - 1][n - 1] == 0:
      return result
    
    visited = [[False] * n for _ in range(n)]
    
    # Directions: D, L, R, U (lexicographic)
    dir_row = [1, 0, 0, -1]
    dir_col = [0, -1, 1, 0]
    dir_char = ['D', 'L', 'R', 'U']

    def backtrack(r, c, path):
      # If reached destination
      if r == n - 1 and c == n - 1:
        result.append(path)
        return
      
      # Mark current cell visited
      visited[r][c] = True

      # Try all 4 directions
      for i in range(4):
        nr = r + dir_row[i]
        nc = c + dir_col[i]

        # Valid move
        if (0 <= nr < n and 0 <= nc < n and mat[nr][nc] == 1 and not visited[nr][nc]):
          backtrack(nr, nc, path + dir_char[i])

      # Unmark (backtrack)
      visited[r][c] = False

    backtrack(0, 0, "")
    return result
  

if __name__ == '__main__':
  sol = Solution()
  print(sol.findPath([[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]))