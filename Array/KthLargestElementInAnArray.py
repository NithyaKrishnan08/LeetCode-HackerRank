# Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Leetcode - 215
# Difficulty - Medium

'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
'''
from typing import List

class Solution:
  # Using sorting
  def findKthLargestBySorting(self, nums: List[int], k: int) -> int:
    nums.sort()
    return nums[len(nums) - k]
    
  # Quick Select Algorithm
  def findKthLargest(self, nums: List[int], k: int) -> int:
    n = len(nums)
    k = n - k

    def quickSelect(left, right):
      pivot, p = nums[right], left
      for i in range(left, right):
        if nums[i] <= pivot:
          nums[i], nums[p] = nums[p], nums[i]
          p += 1
      nums[p], nums[right] = nums[right], nums[p]

      if p > k:
        return quickSelect(left, p - 1)
      elif p < k:
        return quickSelect(p + 1, right)
      else:
        return nums[p]

    return quickSelect(0, n - 1)

if __name__ == "__main__":
  nums = [3,2,1,5,6,4]
  k = 2
  print(Solution().findKthLargestBySorting(nums, k))

  nums = [3,2,1,5,6,4]
  k = 2
  print(Solution().findKthLargestBySorting(nums, k))