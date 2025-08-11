# Longest String Chain
# https://leetcode.com/problems/longest-string-chain/description/
# LeetCode 1048

'''
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

 

Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
Example 3:

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of lowercase English letters.
'''
from typing import List

class Solution:
  # TC: O(N) * N log N
  # SC: O(N)
  def longestStrChain(self, words: List[str]) -> int:
    words.sort(key=len)
    n = len(words)
    dp = [1] * (n)

    def compare_str(longer, shorter):
      n1, n2 = len(longer), len(shorter)

      if n1 != n2 + 1:
        return False
      
      first = second = 0

      while(first < n1):
        if (second < n2 and longer[first] == shorter[second]):
          first += 1
          second += 1
        else:
          first += 1

      if first == n1 and second == n2:
        return True
      
      return False

    for i in range(n):
      for j in range(i):
        if compare_str(words[i], words[j]) and 1 + dp[j] > dp[i]:
          dp[i] = 1 + dp[j]

    return max(dp)
  
if __name__ == "__main__":
  sol = Solution()
  print(sol.longestStrChain(words = ["a","b","ba","bca","bda","bdca"])) # 4
  print(sol.longestStrChain(words = ["xbc","pcxbcf","xb","cxbc","pcxbc"])) # 5
  print(sol.longestStrChain(words = ["abcd","dbqca"])) # 1