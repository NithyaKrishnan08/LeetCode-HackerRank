# Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/description/
# Leetcode: 205
# Difficulty: Easy

'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true
Explanation:
The strings s and t can be made identical by:
Mapping 'e' to 'a'.
Mapping 'g' to 'd'.

Example 2:
Input: s = "foo", t = "bar"
Output: false
Explanation:
The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:
Input: s = "paper", t = "title"
Output: true

Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
'''

class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False
    
    map_st, map_ts = {}, {}

    for ch_s, ch_t in zip(s, t):
      if ch_s in map_st:
        if map_st[ch_s] != ch_t:
          return False
      else:
        map_st[ch_s] = ch_t
      
      if ch_t in map_ts:
        if map_ts[ch_t] != ch_s:
          return False
      else:
        map_ts[ch_t] = ch_s

    return True
  
if __name__ == '__main__':
  sol = Solution()
  print(sol.isIsomorphic(s = "egg", t = "add")) # True
  print(sol.isIsomorphic(s = "foo", t = "bar")) # False
  print(sol.isIsomorphic(s = "paper", t = "title")) # True