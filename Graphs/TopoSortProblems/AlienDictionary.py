# Alien Dictionary
# https://leetcode.com/problems/alien-dictionary/

'''
There is a foreign language which uses the latin alphabet, but the order among letters is not "a", "b", "c" ... "z" as in English.

You receive a list of non-empty strings words from the dictionary, where the words are sorted lexicographically based on the rules of this new language.

Derive the order of letters in this language. If the order is invalid, return an empty string. If there are multiple valid order of letters, return any of them.

A string a is lexicographically smaller than a string b if either of the following is true:

The first letter where they differ is smaller in a than in b.
There is no index i such that a[i] != b[i] and a.length < b.length.
Example 1:

Input: ["z","o"]

Output: "zo"
Explanation:
From "z" and "o", we know 'z' < 'o', so return "zo".

Example 2:

Input: ["hrn","hrf","er","enn","rfnn"]

Output: "hernf"

Explanation:

from "hrn" and "hrf", we know 'n' < 'f'
from "hrf" and "er", we know 'h' < 'e'
from "er" and "enn", we know get 'r' < 'n'
from "enn" and "rfnn" we know 'e'<'r'
so one possibile solution is "hernf"
Constraints:

The input words will contain characters only from lowercase 'a' to 'z'.
1 <= words.length <= 100
1 <= words[i].length <= 100
'''

from collections import defaultdict, deque
from typing import List

# TC: O(V + E)
# SC: O(V + E)

class Solution:
  def foreignDictionary(self, words: List[str]) -> str:
    # Step 1: Build the graph
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    all_chars = set()

    # Initialize all characters and ensuring in_degree is set for all characters
    for word in words:
      for char in word:
        all_chars.add(char)
        in_degree[char] = 0

    # Step 2: Build edges from word pairs
    for i in range(len(words) - 1):
      word1, word2 = words[i], words[i + 1]
      min_length = min(len(word1), len(word2))

      # Edge case: invalid if prefix mismatch
      if len(word1) > len(word2) and word1[:min_length] == word2[:min_length]:
        return ""
      
      for j in range(min_length):
        if word1[j] != word2[j]:
          graph[word1[j]].append(word2[j])
          in_degree[word2[j]] += 1
          break
    
    # Step 3: Topological Sort using Kahn's Algorithm
    queue = deque()
    queue.extend([char for char in all_chars if in_degree[char] == 0])

    topological_order = []

    while queue:
      ch = queue.popleft()
      topological_order.append(ch)

      for neighbor in graph[ch]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
          queue.append(neighbor)

    # check for cycle
    if len(topological_order) != len(all_chars):
      return ""
    
    # Step 4: Return the result
    return ''.join(topological_order)

if __name__ == "__main__":
  words = ["hrn","hrf","er","enn","rfnn"]
  sol = Solution()
  print(sol.foreignDictionary(words))