# Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/description/

'''
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
'''

# Generate all subsequences
# compare on the way

class Solution:
  # Recursion
  # TC: Exponential, O(2^(n1+n2))
  # SC: O(n1+n2) for recursion stack
  def longestCommonSubsequence0(self, text1: str, text2: str) -> int:
    n1= len(text1)
    n2= len(text2)

    def lcs(i1, i2):
      # Base case: if either string is exhausted
      if i1 < 0 or i2 < 0:
        return 0
      
      if text1[i1] == text2[i2]:
        return 1 + lcs(i1-1, i2-1)
      
      return max(lcs(i1-1, i2), lcs(i1, i2-1))
      
    return lcs(n1-1, n2-1)
  
  # Memoization
  # TC: O(n1*n2)
  # SC: O(n1*n2) for dp array + O(n1+n2) for recursion stack
  def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
    n1= len(text1)
    n2= len(text2)
    dp = [[-1 for _ in range(n2)] for _ in range(n1)]

    def lcs(i1, i2):
      # Base case: if either string is exhausted
      if i1 < 0 or i2 < 0:
        return 0
      
      if dp[i1][i2] != -1:
        return dp[i1][i2]
      
      if text1[i1] == text2[i2]:
        dp[i1][i2] = 1 + lcs(i1-1, i2-1)
      else:
        dp[i1][i2] = max(lcs(i1-1, i2), lcs(i1, i2-1))

      return dp[i1][i2]
      
    return lcs(n1-1, n2-1)
  
  # Tabulation
  # TC: O(n1*n2)
  # SC: O(n1*n2) for dp array + O(n1+n2) for recursion stack
  def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
    n1 = len(text1)
    n2 = len(text2)
    dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

    for i1 in range(1, n1 + 1):
      for i2 in range(1, n2 + 1):        
        if text1[i1 - 1] == text2[i2 - 1]:
          dp[i1][i2] = 1 + dp[i1 - 1][i2 - 1]
        else:
          dp[i1][i2] = max(dp[i1 - 1][i2], dp[i1][i2 - 1])
      
    return dp[n1][n2]
  
  # Space Optimized Tabulation
  # TC: O(n1*n2)
  # SC: O(n1*n2) for dp array + O(n1+n2) for recursion stack
  def longestCommonSubsequence3(self, text1: str, text2: str) -> int:
    n1 = len(text1)
    n2 = len(text2)

    prev = [0] * (n2 + 1)
    curr = [0] * (n2 + 1)

    for i1 in range(1, n1 + 1):
      for i2 in range(1, n2 + 1):
        if text1[i1 - 1] == text2[i2 - 1]:
          curr[i2] = 1 + prev[i2 - 1]
        else:
          curr[i2] = max(prev[i2], curr[i2 - 1])
      prev, curr = curr, [0] * (n2 + 1)  # reset curr for next row

    return prev[n2]
  
if __name__ == "__main__":
  # Example usage
  sol = Solution()
  text1 = "abcde"
  text2 = "ace"
  print(sol.longestCommonSubsequence3(text1, text2))