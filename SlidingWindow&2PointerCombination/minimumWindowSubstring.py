# Minimum Window Substring

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
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

'''
from collections import Counter

class Solution:
  def minWindow(self, s: str, t: str) -> str:
    if not s or not t:
      return ""
    
    n = len(s)
    need = Counter(t)
    need_count = len(need)
    window = {}
    have = 0

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

    return s[start: start + min_len] if min_len != float('inf') else ""
  
if __name__ == "__main__":
  s = "ADOBECODEBANC"
  t = "ABC"
  solution = Solution()
  result = solution.minWindow(s, t)
  print(result)

