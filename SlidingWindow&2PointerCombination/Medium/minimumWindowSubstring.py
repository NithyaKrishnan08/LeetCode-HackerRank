'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
'''

from typing import List
from collections import Counter

# Brute force solution
# Time Complexity: O(n^2)
# Space Complexity: O(256)

def minWindow1(s: str, t: str) -> str:
  n = len(s)
  m = len(t)
  start_index = 0
  min_len = float('inf')

  for i in range(n):
    hash_set = [0] * 256
    for j in range(m):
      hash_set[ord(t[j])] += 1
    
    count = 0
    for j in range(i, n):
      if hash_set[ord(s[j])] > 0:
        count += 1
      hash_set[ord(s[j])] -= 1
      
      if count == m:
        if(j - i + 1) < min_len:
          min_len = j - i + 1
          start_index = i
        break

  if min_len == float('inf'):
    return ""

  return s[start_index:start_index + min_len]

# 2 pointers and sliding window
# Optimal solution
# Time Complexity: O(n + n) - n is the size of the hashset
# Space Complexity: O(26)

def minWindow2(s: str, t: str) -> str:
  if not s or not t:
    return ""
  
  n = len(s)
  
  need = Counter(t)
  window = {}
  have = 0
  need_count = len(need)

  left = 0
  start = 0
  min_len = float('inf')

  for right in range(n):
    char1 = s[right]
    window[char1] = window.get(char1, 0) + 1

    if char1 in need and window[char1] == need[char1]:
      have += 1

    while have == need_count:
      if (right - left + 1) < min_len:
        min_len = right - left + 1
        start = left

      char2 = s[left]
      window[char2] -= 1
      if char2 in need and window[char2] < need[char2]:
        have -= 1
      left += 1
  
  return s[start:start + min_len] if min_len != float('inf') else ""

if __name__ == "__main__":
  s = "ADOBECODEBANC"
  t = "ABC"

  # s = "AA"
  # t = "AA"

  # print("Brute force solution")
  # result1 = minWindow1(s, t)
  # print(f"The minimum window substring: {result1}")

  print("Optimal solution")
  result2 = minWindow2(s, t)
  print(f"The minimum window substring: {result2}")