# N-Queens
# https://leetcode.com/problems/n-queens/description/
# Leetcode Problem 51: N-Queens
# Difficulty: Hard

'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively. 

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]

Constraints:
1 <= n <= 9
'''
from typing import List

class Solution:
  def solveNQueens(self, n: int) -> List[List[str]]:
    result = []
    board = [["."] * n for _ in range(n)]

    cols = set()           # columns where queens exist
    diag1 = set()          # r - c  (major diagonal)
    diag2 = set()          # r + c  (minor diagonal)

    def backtrack(row):
      if row == n:
        # convert board to expected string format
        result.append(["".join(r) for r in board])
        return
      
      for col in range(n):
        if col in cols or (row - col) in diag1 or (row + col) in diag2:
          continue  # not safe

        # Place queen
        board[row][col] = "Q"
        cols.add(col)
        diag1.add(row - col)
        diag2.add(row + col)

        backtrack(row + 1)

        # Remove queen (backtrack)
        board[row][col] = "."
        cols.remove(col)
        diag1.remove(row - col)
        diag2.remove(row + col)

    backtrack(0)
    return result
  
if __name__ == '__main__':
  sol = Solution()
  print(sol.solveNQueens(4))
  print(sol.solveNQueens(1))