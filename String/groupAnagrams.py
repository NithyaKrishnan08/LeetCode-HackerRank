'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''

from typing import List
from collections import Counter

# Brute force solution
# Time Complexity: O(n * k * log(k))
# Space Complexity: O(n * k)

def groupAnagrams1(strs: List[str]) -> List[List[str]]:
  result = []
  str_mp = {}

  for i in range(len(strs)):
    s = strs[i]
    s = ''.join(sorted(s))

    if s not in str_mp:
      str_mp[s] = len(result)
      result.append([])

    result[str_mp[s]].append(strs[i])
  return result

# Optimal solution
# Time Complexity: O(n * k * log(k))
# Space Complexity: O(n * k)
MAX_CHAR = 26

def getHash(s):
  hashList = []
  freq = [0] * MAX_CHAR
  
  for ch in s:
      freq[ord(ch) - ord('a')] += 1

  for i in range(MAX_CHAR):
      hashList.append(str(freq[i]))
      hashList.append("$")
  
  return ''.join(hashList)

def groupAnagrams2(strs: List[str]) -> List[List[str]]:
  result = []
  str_mp = {}

  for i in range(len(strs)):
    key = getHash(strs[i])

    if key not in str_mp:
      str_mp[key] = len(result)
      result.append([])

    result[str_mp[key]].append(strs[i])
  return result

if __name__ == "__main__":
  arr = ["act", "god", "cat", "dog", "tac"]
  
  print("Brute force solution")
  res1 = groupAnagrams1(arr)
  for group in res1:
      print(" ".join(group))

  print("Optimal solution")
  res2 = groupAnagrams2(arr)
  for group in res2:
      print(" ".join(group))
