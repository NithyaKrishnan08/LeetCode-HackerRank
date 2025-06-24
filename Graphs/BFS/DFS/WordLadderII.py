# Word Ladder II
# Hard
# LeetCode #126
# https://leetcode.com/problems/word-ladder-ii/

'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 5
endWord.length == beginWord.length
1 <= wordList.length <= 500
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
The sum of all shortest transformation sequences does not exceed 105.
'''

from typing import List
from collections import defaultdict, deque

class Solution:
  def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    wordSet = set(wordList)
    if endWord not in wordSet:
      return []

    # Step 1: BFS to build distance and neighbors
    neighbors = defaultdict(list)
    distance = {beginWord: 0}
    queue = deque([beginWord])

    while queue:
      current = queue.popleft()
      for i in range(len(current)):
        for c in 'abcdefghijklmnopqrstuvwxyz':
          newWord = current[:i] + c + current[i+1:]
          if newWord in wordSet:
            neighbors[current].append(newWord)
            if newWord not in distance:
                distance[newWord] = distance[current] + 1
                queue.append(newWord)

    res = []
    # No path found
    if endWord not in distance:
      return []

    # Step 2: DFS to find all paths
    def dfs(current, path):
      if current == endWord:
        res.append(list(path))
        return
      for nei in neighbors[current]:
        if distance[nei] == distance[current] + 1:  # ensure shortest path
          path.append(nei)
          dfs(nei, path)
          path.pop()

    dfs(beginWord, [beginWord])
    return res
  
if __name__ == "__main__":
  beginWord = "hit"
  endWord = "cog"
  wordList = ["hot","dot","dog","lot","log","cog"]
  sol = Solution()
  print(sol.findLadders(beginWord, endWord, wordList))