# Count Number of Substrings
# Difficulty: Medium

'''
Problem Statement: You are given a string s and a positive integer k.
Return the number of substrings that contain exactly k distinct characters.

Examples
Example 1:  
Input: s = "pqpqs", k = 2  
Output: 7  
Explanation:  All substrings with exactly 2 distinct characters:  
"pq", "pqp", "pqpq", "qp", "qpq", "pqs", "qs"  
Total = 7.

Example 2:  
Input: s = "abcbaa", k = 3  
Output: 5  
Explanation:  All substrings with exactly 3 distinct characters:  
"abc", "abcb", "abcba", "bcba", "cbaa"  
Total = 5.
'''
from collections import defaultdict

class Solution:
  def count_substrings(self, s, k):
    def atmost_k_distinct(s, K):
      left, count = 0, 0
      freq = defaultdict(int)

      for right in range(len(s)):
        freq[s[right]] += 1

        # Shrink window if more than K distinct characters
        while len(freq) > K:
          freq[s[left]] -= 1
          if freq[s[left]] == 0:
            del freq[s[left]]
          left += 1

        count += (right - left + 1)
      
      return count
    
    # Exactly k distinct = atMost(k) - atmost(k - 1)
    return atmost_k_distinct(s, k) - atmost_k_distinct(s, k - 1)
  

if __name__ == '__main__':
  sol = Solution()
  print(sol.count_substrings(s = "pqpqs", k = 2)) # 7
  print(sol.count_substrings(s = "abcbaa", k = 3)) # 8