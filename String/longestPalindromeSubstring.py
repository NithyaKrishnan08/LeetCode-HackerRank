'''
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 
Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
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

def printLongestPalindromeSubstring(s: str) -> str:
  reversed_s = s[::-1]
  result = printLongestCommonSubstring(s, reversed_s)
  return result

if __name__ == "__main__":
  s1 = "babad"
  s2 = "cbbd"

  result1 = printLongestPalindromeSubstring(s1)
  result2 = printLongestPalindromeSubstring(s2)
  
  print(f"The longest palindrome substring in {s1}: {result1}")
  print(f"The longest palindrome substring in {s2}: {result2}")