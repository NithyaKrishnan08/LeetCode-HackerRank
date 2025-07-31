# Longest Palindromic Subsequence
# https://leetcode.com/problems/longest-palindromic-subsequence/description/
# Pre-requisite: Longest Common Subsequence (LCS)
# Reverse the string and find LCS with the original string to get the longest palindromic subsequence.

'''
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
 

Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.
'''

# Generate all subsequences
# compare on the way

class Solution:
  # Tabulation
  # TC: O(n1*n2)
  # SC: O(n1*n2) for dp array + O(n1+n2) for recursion stack
  def longestPalindromeSubseq(self, s: str) -> int:
    n = len(s)
    t = s[::-1]  # Reverse the string to find LCS which is equivalent to the longest palindromic subsequence
    
    def longestCommonSubsequence(text1: str, text2: str) -> int:
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
    
    return longestCommonSubsequence(s, t)
  
if __name__ == "__main__":
  # Example usage
  sol = Solution()
  s = "bbbab"
  print(sol.longestPalindromeSubseq(s))