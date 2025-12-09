# Kth smallest element in an array

import heapq

class Solution:
  # by using sorting
  # Time Complexity: O(n log n)
  def find_kth_smallest_sorting(self, nums, k):
    nums.sort()
    return nums[k - 1]
  
  # by using heap
  # Time Complexity: O(n log k)
  def find_kth_smallest(self, nums, k):
    max_heap = []
    for num in nums:
      heapq.heappush(max_heap, -num)
      if len(max_heap) > k:
        heapq.heappop(max_heap)

    return -max_heap[0]
  
if __name__ == "__main__":
  solution = Solution()

  nums = [3,2,1,5,6,4]
  k = 2
  result = solution.find_kth_smallest_sorting(nums, k)
  print(f"The {k}th smallest element in the array {nums} is: {result}")

  nums = [3,2,3,1,2,4,5,5,6]
  k = 4
  result = solution.find_kth_smallest_sorting(nums, k)
  print(f"The {k}th smallest element in the array {nums} is: {result}")

  nums = [3,2,1,5,6,4]
  k = 2
  result = solution.find_kth_smallest(nums, k)
  print(f"The {k}th smallest element in the array {nums} is: {result}")

  nums = [3,2,3,1,2,4,5,5,6]
  k = 4
  result = solution.find_kth_smallest(nums, k)
  print(f"The {k}th smallest element in the array {nums} is: {result}")