# Palidrome Partitioning
# https://leetcode.com/problems/palindrome-partitioning/description/
# Leetcode Problem 131: Palindrome Partitioning

'''
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"
Output: [["a"]]
 
Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.
'''
from typing import List

class Solution:
  def partition(self, s: str) -> List[List[str]]:
    n = len(s)
    result = []

    def checkPalindrome(start, end, str):
      while start < end:
        if str[start] != str[end]:
          return False
        start += 1
        end -= 1
      return True
    
    def backtrack(start, path):
      if start == len(s):
        result.append(path[:])
        return
      
      for i in range(start, n):
        if checkPalindrome(start, i, s):
          path.append(s[start:i+1])
          backtrack(i+1, path)
          path.pop()

    backtrack(0, [])
    return result
  
if __name__ == "__main__":
  s = Solution()
  print(s.partition("aab"))  # [["a","a","b"],["aa","b"]]
  print(s.partition("a"))    # [["a"]]