# Surrounded Regions

'''
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:


In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]

 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
'''

#  Start from the border Os and mark them that they will not be converted to Xs and convert the rest to Xs.
# TC: O(M * N)
from typing import List

class Solution:
  def solve(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    if not board:
      return
    
    rows, cols = len(board), len(board[0])

    def dfs(r, c):
      # checking the boundaries
      if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
        return
      
      # Mark the cell as safe
      board[r][c] = 'S'

      # Explore all four directions
      dfs(r + 1, c)
      dfs(r - 1, c)
      dfs(r, c + 1)
      dfs(r, c - 1)
      
    # Step 1: Start DFS from the border cells
    # Checking the first and last columns
    for i in range(rows):
      if board[i][0] == 'O':
        dfs(i, 0)
      if board[i][cols - 1] == 'O':
        dfs(i, cols - 1)

    # Checking the first and last rows
    for j in range(cols):
      if board[0][j] == 'O':
        dfs(0, j)
      if board[rows - 1][j] == 'O':
        dfs(rows - 1, j)

    # Step 2: Flip the captured regions to 'X' and restore the safe cells
    for i in range(rows):
      for j in range(cols):
        if board[i][j] == 'O':
          board[i][j] = 'X'
        elif board[i][j] == 'S':
          board[i][j] = 'O'

if __name__ == "__main__":
  board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
  sol = Solution()
  sol.solve(board)
  print(board)