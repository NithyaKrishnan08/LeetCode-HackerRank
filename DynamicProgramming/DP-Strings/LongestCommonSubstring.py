# Longest Common substring
# https://leetcode.com/problems/longest-common-subsequence/description/

'''
Problem Statement: Longest Common Substring

A substring of a string is a subsequence in which all the characters are consecutive. Given two strings, we need to find the longest common substring.

We need to print the length of the longest common substring.

Example 1:
s1 = "abcjklp"
s2 = "acjkp"
Longest common substring: "cjk"
'''
class Solution:
  # Tabulation
  # TC: O(n1*n2)
  # SC: O(n1*n2) for dp array + O(n1+n2) for recursion stack
  def longestCommonSubstring(self, text1: str, text2: str) -> int:
    n1 = len(text1)
    n2 = len(text2)
    dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    max_length = 0

    for i1 in range(1, n1 + 1):
      for i2 in range(1, n2 + 1):
        if text1[i1 - 1] == text2[i2 - 1]:
          dp[i1][i2] = 1 + dp[i1 - 1][i2 - 1]
          max_length = max(max_length, dp[i1][i2])
      
    return max_length
  
if __name__ == "__main__":
  # Example usage
  sol = Solution()
  text1 = "abcjklp"
  text2 = "acjkp"
  print(sol.longestCommonSubstring(text1, text2))