# Longest Substring Without Repeating Characters

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
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''



class Solution:
  # Brute Force Solution
  # T: O(N^2)
  # S: O(256)
  def lengthOfLongestSubstring1(self, s: str) -> int:
    n = len(s)
    max_length = 0
    
    for i in range(n):
      hash_set = [0] * 256
      for j in range(i, n):
        if hash_set[ord(s[j])] == 1:
          break
        max_length = max(max_length, j - i + 1)
        hash_set[ord(s[j])] = 1

    return max_length
  
  # Optimal solution - sliding window and 2 pointer
  # T: O(N)
  # S: O(256)
  def lengthOfLongestSubstring2(self, s: str) -> int:
    n = len(s)
    hash_set = [-1] * 256

    max_length = 0
    left, right = 0, 0

    while right < n:
      if hash_set[ord(s[right])] != -1:
        if hash_set[ord(s[right])] >= left:
          left = hash_set[ord(s[right])] + 1

      length = right - left + 1
      max_length = max(max_length, length)
      hash_set[ord(s[right])] = right
      right += 1

    return max_length
  
if __name__ == "__main__":
  s = "abcabcbb"
  solution = Solution()
  result = solution.lengthOfLongestSubstring2(s)
  print(result)