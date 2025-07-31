# Print Longest Common Subsequence

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
  # Tabulation
  # TC: O(n1*n2)
  # SC: O(n1*n2) for dp array + O(n1+n2) for recursion stack
  def printLongestCommonSubsequence2(self, text1: str, text2: str) -> int:
    n1 = len(text1)
    n2 = len(text2)
    dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

    for i1 in range(n1 + 1):
      for i2 in range(n2 + 1):
        if text1[i1 - 1] == text2[i2 - 1]:
          dp[i1][i2] = 1 + dp[i1 - 1][i2 - 1]
        else:
          dp[i1][i2] = max(dp[i1 - 1][i2], dp[i1][i2 - 1])
      
    # Reconstruct the longest common subsequence
    i, j = n1, n2
    lcs = []

    while i > 0 and j > 0:
      if text1[i - 1] == text2[j - 1]:
        lcs.append(text1[i - 1])
        i -= 1
        j -= 1
      elif dp[i - 1][j] > dp[i][j - 1]:
        i -= 1
      else:
        j -= 1

    lcs.reverse()  # Reverse to get the correct order
    return ''.join(lcs)
  
if __name__ == "__main__":
  # Example usage
  sol = Solution()
  text1 = "abcde"
  text2 = "ace"
  print(sol.printLongestCommonSubsequence2(text1, text2))