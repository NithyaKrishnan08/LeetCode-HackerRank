# Delete Operation for Two Strings
# https://leetcode.com/problems/delete-operation-for-two-strings/description/

'''
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

 

Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4
 

Constraints:

1 <= word1.length, word2.length <= 500
word1 and word2 consist of only lowercase English letters.
'''

class Solution:
  def minDistance(self, word1: str, word2: str) -> int:
    n1 = len(word1)
    n2 = len(word2)

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
    
    lcs = longestCommonSubsequence(word1, word2)
    if lcs == n1 or lcs == n2:
      return abs(n1 - n2)
    
    # Total operations = No. of deletions + No. of insertions
    return (n1 - lcs) + (n2 - lcs)
  
if __name__ == "__main__":
  # Example usage
  sol = Solution()
  word1 = "leetcode"
  word2 = "etco"
  print(sol.minDistance(word1, word2))