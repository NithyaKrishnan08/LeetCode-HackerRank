# Minimum Frequency Elements in Array
# Given an array of integers, find the k elements with the minimum frequency in the array.

import heapq
from collections import Counter

class Solution:
  def k_min_frequency_elements(self, arr, k):
    if k <= 0 or k > len(arr):
      return []

    # Step 1: Calculate frequency of each element
    frequency = Counter(arr)

    # Step 2: Use a min-heap to find the k elements with the minimum frequency
    min_heap = []
    for num, freq in frequency.items():
      heapq.heappush(min_heap, (freq, num))

    # Step 3: Extract the k elements with the minimum frequency
    result = []
    for _ in range(k):
      if min_heap:
        freq, num = heapq.heappop(min_heap)
        result.append(num)

    return result
  
if __name__ == "__main__":
  solution = Solution()

  arr = [4, 1, 2, 2, 3, 3, 3, 4, 4, 4]
  k = 2
  result = solution.k_min_frequency_elements(arr, k)
  print(f"The {k} elements with the minimum frequency in the array are: {result}")