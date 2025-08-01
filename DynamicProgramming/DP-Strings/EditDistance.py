# Edit Distance
# https://leetcode.com/problems/edit-distance/description/
# LeetCode 72

'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
'''

class Solution:
  # Recursion
  # TC: Exponential, O(3^(n1+n2))
  # SC: O(n1+n2) for recursion stack
  def minDistance0(self, word1: str, word2: str) -> int:
    n1, n2 = len(word1), len(word2)

    def paths(i, j):
      if i < 0:
        return j + 1  # If word1 is exhausted, we need j insertions
      if j < 0:
        return i + 1  # If word2 is exhausted, we need i deletions
      
      if word1[i] == word2[j]:
        return paths(i - 1, j - 1)

      insertions = 1 + paths(i, j - 1)  # Insert character
      deletions = 1 + paths(i - 1, j)  # Delete character
      replacements = 1 + paths(i - 1, j - 1) 

      return min(insertions, deletions, replacements)

    return paths(n1 - 1, n2 - 1)
  
  # Memoization
  # TC: O(n1*n2)
  # SC: O(n1*n2) for dp array + O(n1+n2) for recursion stack
  def minDistance1(self, word1: str, word2: str) -> int:
    n1, n2 = len(word1), len(word2)
    dp = [[-1 for _ in range(n2)] for _ in range(n1)]

    def paths(i, j):
      if i < 0:
        return j + 1  # If word1 is exhausted, we need j insertions
      if j < 0:
        return i + 1  # If word2 is exhausted, we need i deletions
      
      if dp[i][j] != -1:
        return dp[i][j]
      
      if word1[i] == word2[j]:
        dp[i][j] = paths(i - 1, j - 1)
        return dp[i][j]

      insertions = 1 + paths(i, j - 1)  # Insert character
      deletions = 1 + paths(i - 1, j)  # Delete character
      replacements = 1 + paths(i - 1, j - 1) 

      dp[i][j] = min(insertions, deletions, replacements)

      return dp[i][j]

    return paths(n1 - 1, n2 - 1)
  
  # Tabulation
  # TC: O(n1*n2)
  # SC: O(n1*n2)
  def minDistance2(self, word1: str, word2: str) -> int:
    n1, n2 = len(word1), len(word2)
    dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

    # Base cases
    for i in range(n1 + 1):
      dp[i][0] = i

    for j in range(n2 + 1):
      dp[0][j] = j

    for i in range(1, n1 + 1):
      for j in range(1, n2 + 1):
        if word1[i - 1] == word2[j - 1]:
          dp[i][j] = dp[i - 1][j - 1]
        else:
          insertions = 1 + dp[i][j - 1]# Insert character
          deletions = 1 + dp[i - 1][j]  # Delete character
          replacements = 1 + dp[i - 1][j - 1] # Replace character

          dp[i][j] = min(insertions, deletions, replacements)

    return dp[n1][n2]

if __name__ == '__main__':
  sol = Solution()
  print(sol.minDistance2(word1="horse", word2 = "ros"))  # Output: 3
  print(sol.minDistance2(word1="intention", word2 = "execution"))  # Output: 5
                
            
        