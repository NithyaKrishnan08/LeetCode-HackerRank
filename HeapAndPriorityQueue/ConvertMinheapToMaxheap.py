# Convert Min Heap to Max Heap and vice versa

import heapq

class Solution:
  def convert_min_heap_to_max_heap(self, min_heap):
    max_heap = [-x for x in min_heap]
    heapq.heapify(max_heap)
    return max_heap
  
  def convert_max_heap_to_min_heap(self, max_heap):
    min_heap = [-x for x in max_heap]
    heapq.heapify(min_heap)
    return min_heap
  
if __name__ == "__main__":
  solution = Solution()

  min_heap = [1, 3, 5, 7, 9, 11]
  heapq.heapify(min_heap)   # ensure it's a valid min-heap
  print("Original Min Heap:", min_heap)
  
  max_heap = solution.convert_min_heap_to_max_heap(min_heap)
  print("Converted Max Heap (simulated):", [-x for x in max_heap])
  
  reverted_min_heap = solution.convert_max_heap_to_min_heap(max_heap)
  print("Reverted Min Heap:", reverted_min_heap)