# Word Ladder I
# Hard
# LeetCode #127
# https://leetcode.com/problems/word-ladder/

'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
'''
from typing import List
from collections import deque

class Solution:
  def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    wordSet = set(wordList)
    if endWord not in wordSet:
      return 0
    
    queue = deque()
    queue.append((beginWord, 1))

    while queue:
      word, level = queue.popleft()

      if word == endWord:
        return level
      
      for i in range(len(word)):
        for c in "abcdefghijklmnopqrstuvwxyz":
          newWord = word[:i] + c + word[i + 1:]
          if newWord in wordSet:
            wordSet.remove(newWord)
            queue.append((newWord, level + 1))

    return 0
  
if __name__ == "__main__":
  beginWord = "hit"
  endWord = "cog"
  wordList = ["hot","dot","dog","lot","log","cog"]
  sol = Solution()
  print(sol.ladderLength(beginWord, endWord, wordList))