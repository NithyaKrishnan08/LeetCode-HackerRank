# Matrix Chain Multiplication

'''
Given an array arr[] which represents the dimensions of a sequence of matrices where the ith matrix has the dimensions (arr[i-1] x arr[i]) for i>=1, find the most efficient way to multiply these matrices together. The efficient way is the one that involves the least number of multiplications.

Examples:

Input: arr[] = [2, 1, 3, 4]
Output: 20
Explanation: There are 3 matrices of dimensions 2 × 1, 1 × 3, and 3 × 4, Let this 3 input matrices be M1, M2, and M3. There are two ways to multiply: ((M1 x M2) x M3) and (M1 x (M2 x M3)), note that the result of (M1 x M2) is a 2 x 3 matrix and result of (M2 x M3) is a 1 x 4 matrix. 
((M1 x M2) x M3)  requires (2 x 1 x 3) + (2 x 3 x 4) = 30 
(M1 x (M2 x M3))  requires (1 x 3 x 4) + (2 x 1 x 4) = 20. 
The minimum of these two is 20.
Input: arr[] = [1, 2, 3, 4, 3]
Output: 30
Explanation: There are 4 matrices of dimensions 1 × 2, 2 × 3, 3 × 4, 4 × 3. Let this 4 input matrices be M1, M2, M3 and M4. The minimum number of multiplications are obtained by ((M1 x M2) x M3) x M4). The minimum number is (1 x 2 x 3) + (1 x 3 x 4) + (1 x 4 x 3) = 30.
Input: arr[] = [3, 4]
Output: 0
Explanation: As there is only one matrix so, there is no cost of multiplication.
Constraints: 
2 ≤ arr.size() ≤ 100
1 ≤ arr[i] ≤ 200
'''

# Partition DP
# Rule 1: Start eith entire block / array => f(i, j)
# Rule 2: Try all partitions -> Run a loop to try all partitionss
# Rule 3: Return the best possible two partitions

class Solution:
  # Recursion
  # TC: O(2^n) exponential
  # SC: O(n)
  def matrixChainMultiplication0(self, arr):
    n = len(arr)

    def find_min_steps(i, j):
      # Base case
      if i == j:
        return 0
      
      min_steps = float('inf')

      # Try all partitions
      for k in range(i, j):
        steps = arr[i - 1] * arr[k] * arr[j] + find_min_steps(i, k) + find_min_steps(k + 1, j)
        min_steps = min(min_steps, steps)

      return min_steps

    return find_min_steps(1, n - 1)
  
  # Memoization
  # TC: O(n^3)
  # SC: O(n^2) + O(N) -> Auxillary Stack Space
  def matrixChainMultiplication1(self, arr):
    n = len(arr)
    dp = [[-1] * n for _ in range(n)]

    def find_min_steps(i, j):
      # Base case
      if i == j:
        return 0
      
      if dp[i][j] != -1:
        return dp[i][j]
      
      min_steps = float('inf')

      # Try all partitions
      for k in range(i, j):
        steps = arr[i - 1] * arr[k] * arr[j] + find_min_steps(i, k) + find_min_steps(k + 1, j)
        min_steps = min(min_steps, steps)

      dp[i][j] = min_steps
      return dp[i][j]

    return find_min_steps(1, n - 1)
  
  # Tabulation
  # Step 1: Copy the base case
  # Step 2: Write down the changing parameters
  # Step 3: Copy the recurrence
  # TC: O(n^3)
  # SC: O(n^2)
  def matrixChainMultiplication2(self, arr):
    n = len(arr)
    dp = [[-1] * n for _ in range(n)]

    for i in range(1, n):
      dp[i][i] = 0

    for i in range(n - 1, 0, -1):
      for j in range(i + 1, n):
        min_steps = float('inf')

        # Try all partitions
        for k in range(i, j):
          steps = arr[i - 1] * arr[k] * arr[j] + dp[i][k] + dp[k + 1][j]
          min_steps = min(min_steps, steps)

        dp[i][j] = min_steps
    
    return dp[1][n - 1]

if __name__ == "__main__":
  sol = Solution()
  print(sol.matrixChainMultiplication2(arr = [10, 20, 30, 40, 50])) # Expected 38000
  print(sol.matrixChainMultiplication2([2, 1, 3, 4]))  # Expected 20
  print(sol.matrixChainMultiplication2([1, 2, 3, 4, 3]))  # Expected 30