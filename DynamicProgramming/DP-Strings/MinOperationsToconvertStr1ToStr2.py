# Minimum Insertions/Deletions to Convert String A to String B

'''
Problem Statement: Minimum Insertions/Deletions to Convert String A to String B

We are given two strings, str1 and str2. We are allowed the following operations:

Delete any number of characters from string str1.
Insert any number of characters in string str1.
We need to tell the minimum operations required to convert str1 to str2.
'''
# Delete any number of characters from string str1.
# Insert any number of characters in string str1.
# We need to tell the minimum operations required to convert str1 to str2.

# What I cannot touch?
# Max no of operations = len(str1) + len(str2)

# No. of deletions = len(str1) - LCS(str1, str2)
# No. of insertions = len(str2) - LCS(str1, str2)
# Total operations = No. of deletions + No. of insertions = len(str1) + len(str2) - 2 * LCS(str1, str2)

class Solution:
  def minInsertionsDeletions(self, s1: str, s2: str) -> int:
    n1 = len(s1)
    n2 = len(s2)

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
    
    lcs = longestCommonSubsequence(s1, s2)
    deletions = n1 - lcs
    insertions = n2 - lcs
    
    # Total operations = No. of deletions + No. of insertions
    return deletions + insertions
  
if __name__ == "__main__":
  # Example usage
  sol = Solution()
  s1 = "abcd"
  s2 = "anc"
  print(sol.minInsertionsDeletions(s1, s2))