# Palindrome Partitioning - II
# https://leetcode.com/problems/palindrome-partitioning-ii/description/
# Leetcode: 132

'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase English letters only.
'''

class Solution:
  # Recursion
  # Time Complexity: O(2^n)
  # Space Complexity: O(n)
  def minCut0(self, s: str) -> int:
    n = len(s)

    def is_palindrome(start, end):
      while start < end:
        if s[start] != s[end]:
          return False
        start += 1
        end -= 1
      return True

    def dfs(start):
      if start >= n:
        return 0
      
      min_cuts = float('inf')

      for end in range(start, n):
        if is_palindrome(start, end):
          cuts = 1 + dfs(end + 1)
          min_cuts = min(min_cuts, cuts)
      return min_cuts

    return dfs(0) - 1
  
  # Memoization
  # Time Complexity: O(n^2)
  # Space Complexity: O(n^2)
  def minCut1(self, s: str) -> int:
    n = len(s)
    dp = [-1] * n

    is_pal = [[False] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
      for j in range(i, n):
        if s[i] == s[j] and (j - i < 2 or is_pal[i + 1][j - 1]):
          is_pal[i][j] = True

    def dfs(start):
      if start >= n:
        return 0
      
      if dp[start] != -1:
        return dp[start]
      
      min_cuts = float('inf')

      for end in range(start, n):
        if is_pal[start][end]:
          cuts = 1 + dfs(end + 1)
          min_cuts = min(min_cuts, cuts)
      
      dp[start] = min_cuts
      return dp[start]

    return dfs(0) - 1
  
  # Tabulation
  # Time Complexity: O(n^2)
  # Space Complexity: O(n^2)
  def minCut2(self, s: str) -> int:
    n = len(s)
    dp = [0] * (n + 1)
    dp[n] = 0

    is_pal = [[False] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
      for j in range(i, n):
        if s[i] == s[j] and (j - i < 2 or is_pal[i + 1][j - 1]):
          is_pal[i][j] = True

    for i in range(n - 1, -1, -1):
      min_cuts = float('inf')
      for j in range(i, n):
        if is_pal[i][j]:
          cuts = 1 + dp[j + 1]
          min_cuts = min(min_cuts, cuts)
      dp[i] = min_cuts

    return dp[0] - 1
    
if __name__ == "__main__":
  sol = Solution()
  print(sol.minCut2("aab"))  # Output: 1
  print(sol.minCut2("a"))    # Output: 0
  print(sol.minCut2("ab"))   # Output: 1
  print(sol.minCut2("bababcbadcede"))   # Output: 4