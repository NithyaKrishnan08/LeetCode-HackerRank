# Evaluate Boolean Expression to True

'''
Problem Statement: Given an expression, A, with operands and operators (OR, AND, XOR), in how many ways can you evaluate the expression to be true, by grouping it in different ways?

Operands are only true and false.

Return the number of ways to evaluate the expression modulo 103 + 3.

Example 1:
Input: expression = “T|T&F”
Output: 1
Explanation: The only way to get the result as true is:
(T) | (T&F) = T|F = T 

Example 2:
Input: expression = “F|T^F”
Output: 2
Explanation: There are 2 possible ways to get the result as true:
		i) (F|T) ^ F = T ^ F = T
		ii) F | (T^F) = F | T = T
'''

class Solution:
  # Recursion
  # TC: Exponential
  # SC: O(n) - recursive stack space
  def countWays0(self, A: str) -> int:
    n = len(A)
    mod = 1000000007

    def count_ways(i, j, is_true):
      if i > j:
        return 0
      
      if i == j:
        if is_true:
          return 1 if A[i] == 'T' else 0
        else:
          return 1 if A[i] == 'F' else 0
      
      ways = 0
      for k in range(i + 1, j, 2):
        left_true = count_ways(i, k - 1, True)
        left_false = count_ways(i, k - 1, False)
        right_true = count_ways(k + 1, j, True)
        right_false = count_ways(k + 1, j, False)

        if A[k] == '&':
          ways += (left_true * right_true) if is_true else (left_false * right_false + left_true * right_false + left_false * right_true)
        elif A[k] == '|':
          ways += (left_true * right_true + left_true * right_false + left_false * right_true) if is_true else (left_false * right_false)
        elif A[k] == '^':
          ways += (left_true * right_false + left_false * right_true) if is_true else (left_true * right_true + left_false * right_false)

        ways %= mod

      return ways

    return count_ways(0, n - 1, True)
  
  # Memoization
  # TC: O(n^3)
  # SC: O(n^2) + O(n) -> Auxillary Stack Space
  def countWays1(self, A: str) -> int:
    n = len(A)
    mod = 1003
    dp = [[[-1] * 2 for _ in range(n)] for _ in range(n)]

    def count_ways(i, j, is_true):
      if i > j:
        return 0
      
      if i == j:
        if is_true:
          return 1 if A[i] == 'T' else 0
        else:
          return 1 if A[i] == 'F' else 0
        
      if dp[i][j][1 if is_true else 0] != -1:
        return dp[i][j][1 if is_true else 0]
      
      ways = 0
      for k in range(i + 1, j, 2):
        left_true = count_ways(i, k - 1, True)
        left_false = count_ways(i, k - 1, False)
        right_true = count_ways(k + 1, j, True)
        right_false = count_ways(k + 1, j, False)

        if A[k] == '&':
          if is_true:
            ways += (left_true * right_true)
          else:
            ways += (left_false * right_false + left_true * right_false + left_false * right_true)
        elif A[k] == '|':
          if is_true:
            ways += (left_true * right_true + left_true * right_false + left_false * right_true)
          else:
            ways += (left_false * right_false)
        elif A[k] == '^':
          if is_true:
            ways += (left_true * right_false + left_false * right_true)
          else:
            ways += (left_true * right_true + left_false * right_false)

        ways %= mod

      dp[i][j][1 if is_true else 0] = ways
      return ways

    return count_ways(0, n - 1, True)
  
if __name__ == '__main__':
  s = Solution()
  print(s.countWays1("T|T&F")) # 1
  print(s.countWays1("F|T^F")) # 2