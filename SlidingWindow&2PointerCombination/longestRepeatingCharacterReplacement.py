# Longest Repeating Character Replacement

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
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
'''

class Solution:
  # Brute Force Solution
  # T: O(N^2)
  # S: O(26)
  def characterReplacement1(self, s: str, k: int) -> int:
    n = len(s)
    max_length = 0
    
    for i in range(n):
      hash_set = [0] * 26
      max_freq = 0
      for j in range(i, n):
        idx = ord(s[j]) - ord('A')
        hash_set[idx] += 1
        max_freq = max(max_freq, hash_set[idx])
        window_length = j - i + 1
        required_changes = window_length - max_freq

        if required_changes <= k:
          max_length = max(max_length, window_length)
        else:
          break

    return max_length
  
  # Optimal Solution
  # T: O(N)
  # S: O(26)
  def characterReplacement(self, s: str, k: int) -> int:
    n = len(s)
    max_length = 0
    hash_set = [0] * 26

    left = 0
    right = 0
    max_freq = 0

    while right < n:
      idx = ord(s[right]) - ord('A')
      hash_set[idx] += 1
      max_freq = max(max_freq, hash_set[idx])

      window_length = right - left + 1
      required_changes = window_length - max_freq

      if required_changes > k:
        left_idx = ord(s[left]) - ord('A')
        hash_set[left_idx] -= 1
        left += 1

      max_length = max(max_length, right - left + 1)
      right += 1

    return max_length

if __name__ == "__main__":
  s = "AABABBA"
  k = 1
  solution = Solution()
  result = solution.characterReplacement(s, k)
  print(result)