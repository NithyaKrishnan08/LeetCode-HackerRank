'''
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
'''

from typing import List

# Brute Force solution
# Time Complexity: O(No. of rows * no. of columns * 4 ^ m * n)
# Space Complexity: O(m * n)
def findWords1(board: List[List[str]], words: List[str]) -> List[str]:
  output = []
  for word in words:
    if wordSearch(board, word):
      output.append(word)

  return output

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
  
# Optimized solution
# Time Complexity: O(No. of rows * no. of columns * 4 ^ m * n)
# Space Complexity: O(m * n)
class TrieNode:
  def __init__(self):
    self.children = {}
    self.is_end = False

  def addWord(self, word):
    node = self
    for ch in word:
      if ch not in node.children:
        node.children[ch] = TrieNode()
      node = node.children[ch]
    node.is_end = True

class Solution:
  def findWords2(self, board: List[List[str]], words: List[str]) -> List[str]:
    root = TrieNode()
    for w in words:
      root.addWord(w)
    
    no_of_rows, no_of_columns = len(board), len(board[0])
    result, visit = set(), set()

    def backtrack(row, column, node, word):
      if (row < 0 or column < 0 or row == no_of_rows or column == no_of_columns or board[row][column] not in node.children or (row, column) in visit):
        return
    
      visit.add((row, column))
      node = node.children[board[row][column]]
      word += board[row][column]
      if node.is_end:
        result.add(word)
      
      backtrack(row + 1, column, node, word)
      backtrack(row - 1, column, node, word)
      backtrack(row, column + 1, node, word)
      backtrack(row, column - 1, node, word)

      visit.remove((row, column))

    for row in range(no_of_rows):
      for column in range(no_of_columns):
        backtrack(row, column, root, "")
    
    return list(result)
        
if __name__ == "__main__":
  board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"], ["i","f","l","v"]]
  words = ["oath","pea","eat","rain"]

  result1 = findWords1(board, words)
  print(result1)

  solution = Solution()
  result2 = solution.findWords2(board, words)
  print(result2)