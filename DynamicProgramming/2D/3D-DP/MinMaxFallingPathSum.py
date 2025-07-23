# Minimum/Maximum Falling Path Sum
# Variable starting and ending points
# Maximum path sum from any cell in the first row to any cell in the last row

'''
Problem statement
You have been given an N*M matrix filled with integer numbers, find the maximum sum that can be obtained from a path starting from any cell in the first row to any cell in the last row.
From a cell in a row, you can move to another cell directly below that row, or diagonally below left or right. So from a particular cell (row, col), we can move in three directions i.e.
Down: (row+1,col)
Down left diagonal: (row+1,col-1)
Down right diagonal: (row+1, col+1)

Constraints :
1 <= T <= 50
1 <= N <= 100
1 <= M <= 100
-10^4 <= matrix[i][j] <= 10^4

Where 'T' is the number of test cases.
Where 'N' is the number of rows in the given matrix, and 'M' is the number of columns in the given matrix.
And, matrix[i][j] denotes the value at (i,j) cell in the matrix.

Time Limit: 1sec
Input 1 :
2
4 4
1 2 10 4
100 3 2 1
1 1 20 2
1 2 2 1
3 3
10 2 3
3 7 2
8 1 5
Output 1 :
105
25
Explanation Of Input 1 :
In the first test case for the given matrix,
The maximum path sum will be 2->100->1->2, So the sum is 105(2+100+1+2).

In the second test case for the given matrix, the maximum path sum will be 10->7->8, So the sum is 25(10+7+8).
Input 2 :
2
3 3
1 2 3
9 8 7
4 5 6
4 6
10 10 2 -13 20 4
1 -9 -81 30 2 5
0 10 4 -79 2 -10
1 -5 2 20 -11 4
Output 2 :
17
74
Explanation Of Input 2 :
In the first test case for the given matrix, the maximum path sum will be 3->8->6, So the sum is 17(3+8+6).

In the second test case for the given matrix, the maximum path sum will be 20->30->4->20, So the sum is 74(20+30+4+20).
'''
class Solution:
  # Recursion
  # TC: 3^(n)
  # SC: O(path length) -> O((m-1) + (n-1))
  # f(i, j) -> max path sum to reach (i, j) from any cell in the first row
  def getMaxPathSum0_util(self, i, j, matrix):
    m = len(matrix)
    n = len(matrix[0])

    if j < 0 or j >= n:
      return -1e9
    
    if i == 0:
      return matrix[i][j]
    
    moving_up = matrix[i][j] + self.getMaxPathSum0_util(i - 1, j, matrix)
    moving_up_left = matrix[i][j] + self.getMaxPathSum0_util(i - 1, j - 1, matrix)
    moving_up_right = matrix[i][j] + self.getMaxPathSum0_util(i - 1, j + 1, matrix)

    return max(moving_up, moving_up_left, moving_up_right)
  
  def getMaxPathSum0(self, matrix):
    m = len(matrix)
    n = len(matrix[0])
    max_path_sum = -1e9

    for j in range(n):
      max_path_sum = max(max_path_sum, self.getMaxPathSum0_util(m - 1, j, matrix))
    
    return max_path_sum
  
  # Memoization
  # TC: O(n * n)
  # SC: O(path length) -> O((m-1) + (n-1)) + O(n * n)
  def getMaxPathSum1_util(self, i, j, matrix, dp):
    m = len(matrix)
    n = len(matrix[0])

    if j < 0 or j >= n:
      return float('-inf')
    
    if i == 0:
      return matrix[i][j]
    
    if dp[i][j] != -1:
      return dp[i][j]
    
    moving_up = matrix[i][j] + self.getMaxPathSum1_util(i - 1, j, matrix, dp)
    moving_up_left = matrix[i][j] + self.getMaxPathSum1_util(i - 1, j - 1, matrix, dp)
    moving_up_right = matrix[i][j] + self.getMaxPathSum1_util(i - 1, j + 1, matrix, dp)

    dp[i][j] = max(moving_up, moving_up_left, moving_up_right)
    return dp[i][j]
  
  def getMaxPathSum1(self, matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[-1 for _ in range(n)] for _ in range(m)]

    max_path = float('-inf')
    for j in range(n):
      max_path = max(max_path, self.getMaxPathSum1_util(m - 1, j, matrix, dp))

    return max_path
  
  # Tabulation
  # TC: O(m * m)
  # SC: O(m * m)
  def getMaxPathSum2(self, matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[-1 for _ in range(n)] for _ in range(m)]

    for j in range(n):
      dp[0][j] = matrix[0][j]

    for i in range(1, m):
      for j in range(n):
        moving_up = dp[i - 1][j]
        moving_up_left = dp[i - 1][j - 1] if j - 1 >= 0 else float('-inf')
        moving_up_right = dp[i - 1][j + 1] if j + 1 < n else float('-inf')

        dp[i][j] = matrix[i][j] + max(moving_up, moving_up_left, moving_up_right)
    
    return max(dp[m - 1])
  
  # Space Optimization
  # TC: O(m * n)
  # SC: O(n)
  def getMaxPathSum3(self, matrix):
    m = len(matrix)
    n = len(matrix[0])

    prev = matrix[0][:]

    for i in range(1, m):
      curr = [0] * n
      for j in range(n):
        moving_up = prev[j]
        moving_up_left = prev[j - 1] if j - 1 >= 0 else float('-inf')
        moving_up_right = prev[j + 1] if j + 1 < n else float('-inf')

        curr[j] = matrix[i][j] + max(moving_up, moving_up_left, moving_up_right)
      prev = curr[:]
    
    return max(prev)
  
if __name__ == "__main__":
  matrix = [
    [1, 2, 10, 4],
    [100, 3, 2, 1],
    [1, 1, 20, 2],
    [1, 2, 2, 1]
  ]
  sol = Solution()

  # Recursion
  # result = sol.getMaxPathSum0(matrix)
  # print(result)

  # Memoization
  # result = sol.getMaxPathSum1(matrix)
  # print(result)

  # Tabulation
  # result = sol.getMaxPathSum2(matrix)
  # print(result)

  # Space Optimization
  result = sol.getMaxPathSum3(matrix)
  print(result)
