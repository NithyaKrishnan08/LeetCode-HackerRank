# Minimum Insertions to Make String Palindrome
# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/description/
# Pre-requisite: Longest Palindromic Subsequence (LPS) and Longest Common Subsequence (LCS)
# To make a string palinrome, we can reverse th estring and attach to the original string.

'''
Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

 

Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.
Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
'''

class Solution:
  def minInsertions(self, s: str) -> int:
    n = len(s)

    # Tabulation
    # TC: O(n1*n2)
    # SC: O(n1*n2) for dp array + O(n1+n2) for recursion stack
    def longestPalindromeSubseq(s: str) -> int:
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
    
    lps_length = longestPalindromeSubseq(s)
    return n - lps_length  # Minimum insertions needed to make the string a palindrome
  
if __name__ == "__main__":
  # Example usage
  sol = Solution()
  s = "leetcode"
  print(sol.minInsertions(s))