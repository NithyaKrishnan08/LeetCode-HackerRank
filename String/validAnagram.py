'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''

from typing import List
from collections import Counter

# 2 pointers and sliding window
# Optimal solution
# Time Complexity: O(n + n) - n is the size of the hashset
# Space Complexity: O(26)

def isAnagram(s: str, t: str) -> bool:
  if len(s) != len(t):
    return False
  
  s_dict = Counter(s)
  t_dict = Counter(t)
  
  if s_dict == t_dict:
    return True

  return False

if __name__ == "__main__":
  s = "anagram"
  t = "nagaram"


  print("Optimal solution")
  result = isAnagram(s, t)
  if result:
    print(f"{t} is an anagram of {s}")
  else:
    print(f"{t} is not an anagram of {s}")