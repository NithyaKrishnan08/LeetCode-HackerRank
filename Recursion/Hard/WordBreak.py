# Word Break
# https://leetcode.com/problems/word-break/description/
# Leetcode Problem 139: Word Break
# Difficulty: Medium

'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
'''

from typing import List

class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    word_set = set(wordDict)
    n = len(s)
    memo = {}

    def backtrack(start):
      # If reached end of string
      if start == n:
        return True
      
      # If already computed
      if start in memo:
        return memo[start]
      
      # Try all possible end positions
      for end in range(start + 1, n + 1):
        word = s[start:end]
        if word in word_set:
          if backtrack(end):
            memo[start] = True
            return True
      
      memo[start] = False
      return False

    return backtrack(0)
  
if __name__ == '__main__':
  sol = Solution()
  print(sol.wordBreak("leetcode", ["leet","code"]))  # True
  print(sol.wordBreak("applepenapple", ["apple","pen"]))  # True
  print(sol.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))  # False