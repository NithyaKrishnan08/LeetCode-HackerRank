# Distinct Subsequences
# https://leetcode.com/problems/distinct-subsequences/
# LeetCode 115

'''
Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

 

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag
 

Constraints:

1 <= s.length, t.length <= 1000
s and t consist of English letters.
'''

class Solution:
  # Recursive approach
  # TC: Exponential, O(2^(m+n))
  # SC: O(m+n) for recursion stack
  def numDistinct0(self, s: str, t: str) -> int:
    m, n = len(s), len(t)

    def count(i: int, j: int) -> int:
      # Base case: if t is empty, there's one way to form it (by choosing nothing)
      if j < 0:
        return 1
      # If s is empty but t is not, there's no way to form t
      if i < 0:
        return 0
      
      if s[i] == t[j]:
        return count(i - 1, j - 1) + count(i - 1, j)
      else:
        return count(i - 1, j)

    return count(m - 1, n - 1)
  
  # Memoization approach
  # TC: O(m*n)
  # SC: O(m*n) + O(m+n) for recursion stack
  def numDistinct1(self, s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [[-1] * n for _ in range(m)]

    def count(i: int, j: int) -> int:
      # Base case: if t is empty, there's one way to form it (by choosing nothing)
      if j < 0:
        return 1
      # If s is empty but t is not, there's no way to form t
      if i < 0:
        return 0
      
      if dp[i][j] != -1:
        return dp[i][j]
      
      if s[i] == t[j]:
        dp[i][j] = count(i - 1, j - 1) + count(i - 1, j)
      else:
        dp[i][j] = count(i - 1, j)

      return dp[i][j]

    return count(m - 1, n - 1)
  
  # Tabulation approach
  # TC: O(m*n)
  # SC: O(m*n)
  def numDistinct2(self, s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base case: An empty t ("") can always be formed from any prefix of s by deleting all characters
    for i in range(m + 1):
      dp[i][0] = 1

    # Fill the dp table
    for i in range(1, m + 1):
      for j in range(1, n + 1):
        if s[i - 1] == t[j - 1]:
          # Option 1: Match the current character
          # Option 2: Skip the current character in s
          dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        else:
          # Option 2: Skip the current character in s
          dp[i][j] = dp[i - 1][j]

    return dp[m][n]
  
  # Space optimization
  # TC: O(m*n)
  # SC: O(m*n)
  def numDistinct3(self, s: str, t: str) -> int:
    m, n = len(s), len(t)
    prev = [0] * (n + 1)

    # Base case: An empty t ("") can always be formed from any prefix of s by deleting all characters
    prev[0] = 1

    for i in range(1, m + 1):
      for j in range(n, 0, -1):
        if s[i - 1] == t[j - 1]:
          prev[j] += prev[j - 1]


    return prev[n]
  
if __name__ == '__main__':
  sol = Solution()
  s1 = "rabbbit"
  t1 = "rabbit"
  print(sol.numDistinct3(s1, t1))  # Output: 3

  s2 = "babgbag"
  t2 = "bag"
  print(sol.numDistinct3(s2, t2))  # Output: 5