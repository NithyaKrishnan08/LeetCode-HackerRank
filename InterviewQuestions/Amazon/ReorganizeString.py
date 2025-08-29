# Reorganize String
# https://leetcode.com/problems/reorganize-string/description/?envType=problem-list-v2&envId=7p5x763&sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJGUkVRVUVOQ1kifV0%3D&page=1
# Leetcode Problem 767: Reorganize String

'''
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
'''
import heapq
from collections import Counter

class Solution:
  def reorganizeString(self, s: str) -> str:
    # Step 1: Count frequencies
    freq = Counter(s)
    n = len(s)
    
    # Step 2: Check if valid arrangement is possible
    if max(freq.values()) > (n + 1) // 2:
        return ""
    
    # Step 3: Build max heap (use negative counts for max behavior)
    max_heap = [(-count, char) for char, count in freq.items()]
    heapq.heapify(max_heap)
    
    result = []
    
    # Step 4: Greedy placement
    while len(max_heap) > 1:
      count1, char1 = heapq.heappop(max_heap)
      count2, char2 = heapq.heappop(max_heap)
      
      result.extend([char1, char2])
      
      if count1 + 1 < 0:
        heapq.heappush(max_heap, (count1 + 1, char1))
      if count2 + 1 < 0:
        heapq.heappush(max_heap, (count2 + 1, char2))
    
    # Step 5: Add leftover char (if any)
    if max_heap:
      result.append(max_heap[0][1])
    
    return "".join(result)
  
if __name__ == "__main__":
  s = Solution()
  print(s.reorganizeString("aab"))   # "aba"
  print(s.reorganizeString("aaab"))  # ""