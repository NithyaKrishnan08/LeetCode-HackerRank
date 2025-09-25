# Heap operations using Python's heapq module

# Heapq implements a min-heap by default
# To simulate a max-heap, we can insert negative values

import heapq
from collections import Counter

class Solution:
  # Build Min Heap (Heapify)
  # Time Complexity: O(n)
  # Space Complexity: O(1)
  def build_min_heap(self, arr):
    heapq.heapify(arr)
    return arr
  
  # Heap push(Insert element)
  # Time Complexity: O(log n)
  def min_heap_push(self, arr, element):
    heapq.heappush(arr, element)
    return arr
  
  # Heap pop(Extract min element)
  # Time Complexity: O(log n)
  def min_heap_pop(self, arr):
    min_element = heapq.heappop(arr)
    return min_element, arr
  
  # Heap push pop(Push element and pop min element)
  # Time Complexity: O(log n)
  def min_heap_push_pop(self, arr, element):
    min_element = heapq.heappushpop(arr, element)
    return min_element, arr
  
  # Heap peep(Peek min element)
  # Time Complexity: O(1)
  def min_heap_peek(self, arr):
    return arr[0]
  
  # Heap sort (Extract min element repeatedly)
  # Time Complexity: O(n log n)
  # Space Complexity: O(n)
  # Note: O(1) space is possible via swapping, but this is complex
  def min_heap_sort(self, arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0] * n

    for i in range(n):
      min_elem = heapq.heappop(arr)
      new_list[i] = min_elem

    return new_list
  
  # Build Max Heap (Heapify)
  # Time Complexity: O(n)
  # Space Complexity: O(1)
  def build_max_heap(self, arr):
    n = len(arr)
    for i in range(n):
      arr[i] = -arr[i]

    heapq.heapify(arr)
    return arr
  
  # Heap push(Insert element)
  # Time Complexity: O(log n)
  def max_heap_push(self, arr, element):
    heapq.heappush(arr, -element)
    return arr
  
  # Heap pop(Extract max element)
  # Time Complexity: O(log n)
  def max_heap_pop(self, arr):
    max_element = -heapq.heappop(arr)
    return max_element, arr
  
if __name__ == "__main__":
  solution = Solution()

  print("----- Min Heap Operations -----")

  arr = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
  min_heap = solution.build_min_heap(arr)
  print("Min Heap:", min_heap)

  solution.min_heap_push(min_heap, 4)
  print("Min Heap after inserting 4:", min_heap)

  min_elem, min_heap = solution.min_heap_pop(min_heap)
  print("Minimum element in heap:", min_elem)
  print("Min Heap after popping:", min_heap)

  min_elem, min_heap = solution.min_heap_push_pop(min_heap, 99)
  print("Minimum element in heap:", min_elem)
  print("Min Heap after popping:", min_heap)

  min_elem = solution.min_heap_peek(min_heap)
  print("Minimum element in heap:", min_elem)

  arr_2 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
  sorted_arr = solution.min_heap_sort(arr_2)
  print("Sorted array using heap sort:", sorted_arr)

  print("----- Max Heap Operations -----")
  
  arr = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
  max_heap = solution.build_max_heap(arr)
  print("Max Heap:", max_heap)

  solution.max_heap_push(max_heap, 7)
  print("Max Heap after inserting 7:", max_heap)

  max_elem, max_heap = solution.max_heap_pop(max_heap)
  print("Maximum element in heap:", max_elem)
  print("Max Heap after popping:", max_heap)


