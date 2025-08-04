# Wildcard Matching
# https://leetcode.com/problems/wildcard-matching/description/
# LeetCode 44

'''
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
 

Constraints:

0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.
'''

class Solution:
  # Recursion
  # TC: Exponential, O(2^(m+n))
  # SC: O(m+n) for recursion stack
  def isMatch0(self, s: str, p: str) -> bool:
    m, n = len(s), len(p)
    
    def match(i, j) -> bool: # i -> pointer for s, j -> pointer for p
      # Base case: if both strings are exhausted
      if i < 0 and j < 0:
        return True
      
      # s exhausted, p not exhausted
      if i < 0 and j >= 0:
        # p should contain only '*' to match empty s
        for k in range(j + 1):
          if p[k] != '*':
            return False
        return True
      
      # p exhausted, s not exhausted
      if j < 0 and i >= 0:
        return False

      # If chars match or pattern has '?'
      if s[i] == p[j] or p[j] == '?':
        return match(i - 1, j - 1)
      
      # If pattern has '*'
      if p[j] == '*':
        # '*' can match zero characters (move to next char in p) or one or more characters (move to next char in s)
        return match(i - 1, j) or match(i, j - 1)
      
      return False
    
    return match(m - 1, n - 1)
  
  # Memoization
  # TC: O(m*n)
  # SC: O(m*n) + O(m+n) for recursion stack
  def isMatch1(self, s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    
    def match(i, j) -> bool: # i -> pointer for s, j -> pointer for p
      # Base case: if both strings are exhausted
      if i < 0 and j < 0:
        return True
      
      # s exhausted, p not exhausted
      if i < 0 and j >= 0:
        # p should contain only '*' to match empty s
        for k in range(j + 1):
          if p[k] != '*':
            return False
        return True
      
      # p exhausted, s not exhausted
      if j < 0 and i >= 0:
        return False
      
      if dp[i][j] != -1:
        return dp[i][j]

      # If chars match or pattern has '?'
      if s[i] == p[j] or p[j] == '?':
        dp[i][j] = match(i - 1, j - 1)
      
      # If pattern has '*'
      elif p[j] == '*':
        # '*' can match zero characters (move to next char in p) or one or more characters (move to next char in s)
        dp[i][j] = match(i - 1, j) or match(i, j - 1)
      
      else:
        dp[i][j] = False
      
      return dp[i][j]
    
    return match(m - 1, n - 1)
  
  # Tabulation
  # TC: O(m*n)
  # SC: O(m*n)
  def isMatch2(self, s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]

    # Base case: if both strings are exhausted
    dp[0][0] = True
    
    # Base case: s is empty, p can match only if all '*' till index j-1
    for j in range(1, n + 1):
      if p[j - 1] == '*':
        dp[0][j] = dp[0][j - 1]
    
    # Fill the dp table
    for i in range(1, m + 1):
      for j in range(1, n + 1):
        # If chars match or pattern has '?'
        if s[i - 1] == p[j - 1] or p[j - 1] == '?':
          dp[i][j] = dp[i - 1][j - 1]
        
        # If pattern has '*'
        elif p[j - 1] == '*':
          # '*' can match zero characters (move to next char in p) or one or more characters (move to next char in s)
          dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        
        else:
          dp[i][j] = False
    
    return dp[m][n]
    
if __name__ == '__main__':
  sol = Solution()
  print(sol.isMatch2(s="aa", p = "a"))  # Output: false
  print(sol.isMatch2(s="aa", p = "*"))  # Output: true
  print(sol.isMatch2(s="cb", p = "?a")) # Output: false
  print(sol.isMatch2("adceb", "*a*b"))  # True
  print(sol.isMatch2("acdcb", "a*c?b")) # False
