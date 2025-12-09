# Sort K Sorted Array
# Difficulty: Medium

'''
Problem Statement: Given an array arr[] and a number k . The array is sorted in a way that every element is at max k distance away from it sorted position. It means if we completely sort the array, then the index of the element can go from i - k to i + k where i is index in the given array. Our task is to completely sort the array.

Examples
Input :  arr = [6, 5, 3, 2, 8, 10, 9], k = 3  
Output :  [2, 3, 5, 6, 8, 9, 10]  
Explanation :  The element 2 was at index 3, it moved to index 0. The element 3 was at index 2, it moved to index 1. The element 5 moved from index 1 to index 2. The element 6 moved from index 0 to index 3. The rest (8, 9, 10) were near their correct spots and shifted slightly.

Input :  arr = [1, 4, 5, 2, 3, 6, 7, 8, 9, 10], k = 2  
Output :  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
Explanation :  The element 2 moved from index 3 to index 1. The element 3 moved from index 4 to index 2. The element 4 moved from index 1 to index 3. The element 5 moved from index 2 to index 4. All others remained in or near their correct positions.
'''
import heapq

class Solution:
  def sort_k_sorted_array(self, arr, k):
    min_heap = []
    sorted_index = 0

    # Build the initial min-heap with the first k+1 elements
    for i in range(min(k + 1, len(arr))):
      heapq.heappush(min_heap, arr[i])

    # Process the remaining elements
    for i in range(k + 1, len(arr)):
      arr[sorted_index] = heapq.heappop(min_heap)
      sorted_index += 1
      heapq.heappush(min_heap, arr[i])

    # Extract remaining elements from the heap
    while min_heap:
      arr[sorted_index] = heapq.heappop(min_heap)
      sorted_index += 1

    return arr
  
if __name__ == "__main__":
  solution = Solution()

  arr = [6, 5, 3, 2, 8, 10, 9]
  k = 3
  result = solution.sort_k_sorted_array(arr, k)
  print(f"The sorted array of the k-sorted array {arr} with k={k} is: {result}")

  arr = [1, 4, 5, 2, 3, 6, 7, 8, 9, 10]
  k = 2
  result = solution.sort_k_sorted_array(arr, k)
  print(f"The sorted array of the k-sorted array {arr} with k={k} is: {result}")
