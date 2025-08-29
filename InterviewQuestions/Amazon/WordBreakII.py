# Word Break II
# https://leetcode.com/problems/word-break-ii/description/?envType=problem-list-v2&envId=7p5x763&sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJGUkVRVUVOQ1kifV0%3D&page=1
# Leetcode Problem 140: Word Break II

'''
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
 

Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
Input is generated in a way that the length of the answer doesn't exceed 105.
'''
from typing import List

class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    wordSet = set(wordDict)
    n = len(s)
    memo = {}

    def dfs(start):
      if start == n:
        return [""]
      
      if start in memo:
        return memo[start]
      
      sentenses = []
      for end in range(start+1, n+1):
        word = s[start:end]
        if word in wordSet:
          for sub in dfs(end):
            if sub:
              sentenses.append(word + " " + sub)
            else:
              sentenses.append(word)

      memo[start] = sentenses
      return sentenses
    
    return dfs(0)
  
if __name__ == "__main__":
  s = Solution()
  print(s.wordBreak("catsanddog", ["cat","cats","and","sand","dog"]))  # ["cats and dog","cat sand dog"]
  print(s.wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]))  # ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
  print(s.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))  # []
            