'''
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

# 2 pointers and sliding window
from typing import List

# Brute force solution
# Time Complexity: O(n^2)
# Space Complexity: O(256)

def lengthOfLongestSubstring1(string) -> int:
  n = len(string)
  max_length = 0
  for i in range(n):
    hash_set = [0] * 256
    for j in range(i, n):
      if hash_set[ord(string[j])] == 1:
        break
      substring_length = j - i + 1
      max_length = max(max_length, substring_length)
      hash_set[ord(string[j])] = 1

  return max_length

# Optimal solution
# Time Complexity: O(n) - n is the size of the hashset
# Space Complexity: O(n)

def lengthOfLongestSubstring2(string) -> int:
  n = len(string)
  hash_set = [-1] * 256

  max_length = 0
  left = 0
  right = 0

  while right < n:
    if hash_set[ord(string[right])] != -1:
      left = max(hash_set[ord(string[right])] + 1, left)

    hash_set[ord(string[right])] = right
    max_length = max(max_length, right - left + 1)
    right += 1
  
  return max_length

if __name__ == "__main__":
  s = "bbbbbb"

  print("Brute force solution")
  result = lengthOfLongestSubstring1(s)
  print(f"The length of longest substring: {result}")

  print("Optimal solution")
  result = lengthOfLongestSubstring2(s)
  print(f"The length of longest substring: {result}")