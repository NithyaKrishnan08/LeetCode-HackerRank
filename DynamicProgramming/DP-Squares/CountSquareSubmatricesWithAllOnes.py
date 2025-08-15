# Count Square Submatrices with All Ones
# https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/
# LeetCode Problem 1277

'''
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
'''
# The dp table states how many squares can be formed with the bottom-right corner at (i, j).

from typing import List

class Solution:
  # TC: O(rows * cols)
  # SC: O(rows * cols)
  def countSquares(self, matrix: List[List[int]]) -> int:
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    
    total_squares = 0
    
    for i in range(rows):
      for j in range(cols):
        if matrix[i][j] == 1:
          if i == 0 or j == 0:
            dp[i][j] = 1
          else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        
          total_squares += dp[i][j]
    
    return total_squares

if __name__ == '__main__':    
  sol = Solution()
  print(sol.countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]])) # Output: 15
  print(sol.countSquares([[1,0,1],[1,1,0],[1,1,0]])) # Output: 7
        