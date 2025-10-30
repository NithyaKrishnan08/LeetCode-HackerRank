'''
Problem Statement: Introduction to DP on Strings - Longest Common Subsequence

In the coming articles, we will discuss problems related to ‘Dynamic Programming on Strings’. We will discuss the problem of ‘Longest Common Subsequence’ in this article. Before proceeding further, let us understand what is the “Longest Common Subsequence”, or rather what is a “subsequence”?

A subsequence of a string is a list of characters of the string where some characters are deleted ( or not deleted at all) and they should be in the same order in the subsequence as in the original string.

For eg:


Strings like “cab”,” bc” will not be called as a subsequence of “abc” as the characters are not coming in the same order.

Note: For a string of length n, the number of subsequences will be 2n.

Now we will look at “Longest Common Subsequence”. The longest Common Subsequence is defined for two strings. It is the common subsequence that has the greatest length.
'''

from typing import List
from collections import Counter

# Memoization solution
# Time Complexity: O(n * m)
# Space Complexity: O(n * m) + O(n + m)

def dpLongestCommonSubstring(i: int, j: int, s: str, t: str, dp) -> int:
  if i < 0 or j < 0:
    return 0
  
  if dp[i][j] != -1:
    return dp[i][j]
  
  if s[i] == t[j]:
    dp[i][j] = 1 + dpLongestCommonSubstring(i - 1, j - 1, s, t, dp)
  else:
    dp[i][j] = max(dpLongestCommonSubstring(i - 1, j, s, t, dp), dpLongestCommonSubstring(i, j - 1, s, t, dp))
  
  return dp[i][j]
  
def longestCommonSubstring1(s: str, t: str) -> int:
  n = len(s)
  m = len(t)

  dp = [[-1 for j in range(m)] for i in range(n)]

  if n == 0 or m == 0:
    return 0

  return dpLongestCommonSubstring(n - 1, m - 1, s, t, dp)

# Tabulation approach
# Time Complexity: O(n * m)
# Space Complexity: O(n * m) + O(n + m)

def dpLongestCommonSubstring(i: int, j: int, s: str, t: str, dp) -> int:
  if i < 0 or j < 0:
    return 0
  
  if dp[i][j] != -1:
    return dp[i][j]
  
  
  
  return dp[i][j]
  
def longestCommonSubstring2(s: str, t: str) -> int:
  n = len(s)
  m = len(t)

  dp = [[-1 for j in range(m + 1)] for i in range(n + 1)]

  if n == 0 or m == 0:
    return 0
  
  for j in range(m + 1):
    dp[0][j] = 0

  for i in range(n + 1):
    dp[i][0] = 0

  for i in range(1, n + 1):
    for j in range(1, m + 1):
      if s[i - 1] == t[j - 1]:
        dp[i][j] = 1 + dp[i - 1][j - 1]
      else:
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

  return dp[i][j]


if __name__ == "__main__":
  s = "acd"
  t = "ced"

  # print("Memoization solution")
  # result1 = longestCommonSubstring1(s, t)
  
  # print(f"The length of longest common subsequence in {s} and {t}: {result1}")

  print("Tabulation method")
  result2 = longestCommonSubstring2(s, t)
  
  print(f"The length of longest common subsequence in {s} and {t}: {result2}")