# Shortest Common Supersequence
# https://leetcode.com/problems/shortest-common-supersequence/description/
# LeetCode 1092

'''
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

 

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
Example 2:

Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
'''

class Solution:
  # TC: O(n1*n2)
  # SC: O(n1*n2)
  def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
    n1 = len(str1)
    n2 = len(str2)
    dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

    for i1 in range(1, n1 + 1):
      for i2 in range(1, n2 + 1):
        if str1[i1 - 1] == str2[i2 - 1]:
          dp[i1][i2] = 1 + dp[i1 - 1][i2 - 1]
        else:
          dp[i1][i2] = max(dp[i1 - 1][i2], dp[i1][i2 - 1])
      
    # Reconstruct the shortest common supersubsequence
    i, j = n1, n2
    result = []

    while i > 0 and j > 0:
      if str1[i - 1] == str2[j - 1]:
        result.append(str1[i - 1])
        i -= 1
        j -= 1
      elif dp[i - 1][j] > dp[i][j - 1]:
        result.append(str1[i - 1])
        i -= 1
      else:
        result.append(str2[j - 1])
        j -= 1

    while i > 0:
      result.append(str1[i - 1])
      i -= 1

    while j > 0:
      result.append(str2[j - 1])
      j -= 1

    result.reverse()  # Reverse to get the correct order
    return ''.join(result)  
  
if __name__ == "__main__":
  # Example usage
  sol = Solution()
  text1 = "abac"
  text2 = "cab"
  print(sol.shortestCommonSupersequence(text1, text2))