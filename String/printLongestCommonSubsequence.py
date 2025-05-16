'''
Problem Statement: 

Print Longest Common Subsequence
For eg:


Strings like “cab”,” bc” will not be called as a subsequence of “abc” as the characters are not coming in the same order.

Note: For a string of length n, the number of subsequences will be 2n.

Now we will look at “Longest Common Subsequence”. The longest Common Subsequence is defined for two strings. It is the common subsequence that has the greatest length.
'''

from typing import List
from collections import Counter

# Tabulation approach
# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
def printLongestCommonSubstring(s: str, t: str) -> str:
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

  string_len = dp[i][j]
  result = ""
  for i in range(string_len):
    result += "$"

  index = string_len - 1
  i, j = n, m
  while i > 0 and j > 0:
    if(s[i - 1] == t[j - 1]):
      result = s[i - 1] + result[:-1]
      index -= 1
      i -= 1
      j -= 1
    elif dp[i - 1][j] > dp[i][j - 1]:
      i -= 1
    else:
      j -= 1

  return result

if __name__ == "__main__":
  s = "abcde"
  t = "bdgek"

  print("Tabulation method")
  result = printLongestCommonSubstring(s, t)
  
  print(f"The longest common subsequence in {s} and {t}: {result}")