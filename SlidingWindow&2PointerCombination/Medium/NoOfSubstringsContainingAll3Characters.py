# Number of Substrings Containing All Three Characters
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/
# Leetcode: 1358
# Difficulty: Medium

'''
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1
 

Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
'''

class Solution:
  # Brute force solution
  # TC: O(N^2)
  # SC: O(3)
  def numberOfSubstrings1(self, s: str) -> int:
    n = len(s)
    count = 0
    for i in range(n):
      hash_set = [0] * 3
      for j in range(i, n):
        hash_set[ord(s[j]) - ord('a')] = 1
        if hash_set[0] + hash_set[1] + hash_set[2] == 3:
          count = count + (n - j)
          break
        
    return count
  
  # Optimal solution
  # TC: O(N)
  # SC: O(3)
  def numberOfSubstrings2(self, s: str) -> int:
    n = len(s)
    count = 0
    last_seen = [-1] * 3
    for i in range(n):
      last_seen[ord(s[i]) - ord('a')] = i
      if last_seen[0] != -1 and last_seen[1] != -1 and last_seen[2] != -1:
        count = count + 1 + min(last_seen[0], last_seen[1], last_seen[2])
        
    return count
  
  # Optimal solution
  # TC: O(N)
  # SC: O(3)
  def numberOfSubstrings(self, s: str) -> int:
    n = len(s)
    count = {'a': 0, 'b': 0, 'c': 0}
    left = 0
    result = 0
    
    for right in range(n):
      count[s[right]] += 1
      
      while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
        result += n - right
        count[s[left]] -= 1
        left += 1
        
    return result
  
if __name__ == "__main__":
  s = "abcabc"
  solution = Solution()
  result = solution.numberOfSubstrings(s)
  print(result)