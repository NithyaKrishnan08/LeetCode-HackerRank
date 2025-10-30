'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
'''

# 2 pointers and sliding window
from typing import List

# Brute force solution
# Time Complexity: O(n^2)
# Space Complexity: O(26)

def lengthOfLongestRepeatingSubstring1(s: str, k: int) -> int:
  n = len(s)
  max_length = 0
  for i in range(n):
    hash_set = [0] * 26
    max_frequency = 0
    for j in range(i, n):
      hash_set[ord(s[j]) - ord('A')] += 1
      max_frequency = max(max_frequency, hash_set[ord(s[j]) - ord('A')])
      changes = (j - i + 1) - max_frequency
      if changes <= k:
        substring_length = j - i + 1
        max_length = max(max_length, substring_length)
      else:
        break
  return max_length

# Optimal solution
# Time Complexity: O(n + n) - n is the size of the hashset
# Space Complexity: O(26)

def lengthOfLongestRepeatingSubstring2(s: str, k: int) -> int:
  n = len(s)
  hash_map = [0] * 26

  max_length = 0
  max_frequency = 0
  left = 0

  for right in range(n):
    idx = ord(s[right]) - ord('A')
    hash_map[idx] += 1
    max_frequency = max(max_frequency, hash_map[idx])

    # Check if we need to shrink the window
    while (right - left + 1) - max_frequency > k:
      hash_map[ord(s[left]) - ord('A')] -= 1
      left += 1  # shrink the window

    max_length = max(max_length, right - left + 1)

  return max_length

if __name__ == "__main__":
  s = "AABABBA"
  k = 1

  # print("Brute force solution")
  # result1 = lengthOfLongestRepeatingSubstring1(s, k)
  # print(f"The length of longest repeating substring: {result1}")

  print("Optimal solution")
  result2 = lengthOfLongestRepeatingSubstring2(s, k)
  print(f"The length of longest repeating substring: {result2}")