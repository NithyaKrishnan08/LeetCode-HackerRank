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

# Optimal solution
# Time Complexity: O(No. of rows * no. of columns * 4 ^ length of word)
# Space Complexity: O(1)

def wordSearch(board: List[List[str]], word: str) -> bool:
  no_of_rows, no_of_columns = len(board), len(board[0])
  path = set()

  def search(row, column, index):
    if index == len(word):
      return True
    
    if (row < 0 or column < 0 or row >= no_of_rows or column >= no_of_columns or word[index] != board[row][column] or (row, column) in path):
      return False
    
    path.add((row, column))
    result = search(row + 1, column, index + 1) or search(row - 1, column, index + 1) or search(row, column + 1, index + 1) or search(row, column - 1, index + 1)
    
    path.remove((row, column))
    return result
  
  for row in range(no_of_rows):
    for column in range(no_of_columns):
      if search(row, column, 0):
        return True
  
  return False
  
if __name__ == "__main__":
  board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
  word = "ABCCED"

  result = wordSearch(board, word)
  print(result)
  if result:
    print(f"The word {word} exists in the board.")
  else:
    print(f"The word {word} is not found in the board.")