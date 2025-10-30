# Sum of Beauty of All Substrings
# https://leetcode.com/problems/sum-of-beauty-of-all-substrings/description/
# Leetcode: 1781
# Difficulty: Medium

'''
The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string s, return the sum of beauty of all of its substrings.

 

Example 1:

Input: s = "aabcb"
Output: 5
Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
Example 2:

Input: s = "aabcbaa"
Output: 17
 

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters.
'''

class Solution:
  def beautySum(self, s: str) -> int:
    n = len(s)
    total_beauty = 0

    for i in range(n):
      freq = [0] * 26

      for j in range(i, n):
        freq[ord(s[j]) - ord('a')] += 1

        max_freq = 0
        min_freq = float('inf')

        for f in freq:
          if f > 0:
            max_freq = max(max_freq, f)
            min_freq = min(min_freq, f)

        total_beauty += (max_freq - min_freq)

    return total_beauty
  
if __name__ == "__main__":
  s = "aabcb"
  print(Solution().beautySum(s))  # Output: 5

  s = "aabcbaa"
  print(Solution().beautySum(s))  # Output: 17