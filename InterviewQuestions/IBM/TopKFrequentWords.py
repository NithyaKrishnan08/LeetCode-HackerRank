# Top K Frequent Words
# https://leetcode.com/problems/top-k-frequent-words/description/
# Leetcode: 692

'''
Given an array of strings words and an integer k, return the k most frequent strings.
Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.
 

Example 1:
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:
Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
 

Constraints:
1 <= words.length <= 500
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]
'''
from typing import List
from collections import Counter
import heapq

class Solution:
  def topKFrequent(self, words: List[str], k: int) -> List[str]:
    frequency_map = Counter(words)
    sorted_words = sorted(frequency_map.keys(), key=lambda word:(-frequency_map[word], word))

    return sorted_words[:k]
  
  # Using heapq
  def topKFrequent2(self, words: List[str], k: int) -> List[str]:
    frequency_map = Counter(words)
    heap = [(-count, word) for word, count in frequency_map.items()]
    heapq.heapify(heap)

    result = [heapq.heappop(heap)[1] for _ in range(k)]
    return result
  
if __name__ == "__main__":
  solution = Solution()
  words = ["i","love","leetcode","i","love","coding"]
  k = 2
  print(f"Input: words = {words}, k = {k}")
  print(f"Output: {solution.topKFrequent(words, k)}")

  words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
  k = 4
  print(f"Input: words = {words}, k = {k}")
  print(f"Output: {solution.topKFrequent(words, k)}")

  words = ["i","love","leetcode","i","love","coding"]
  k = 2
  print(f"Input: words = {words}, k = {k}")
  print(f"Output: {solution.topKFrequent2(words, k)}")

  words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
  k = 4
  print(f"Input: words = {words}, k = {k}")
  print(f"Output: {solution.topKFrequent2(words, k)}")