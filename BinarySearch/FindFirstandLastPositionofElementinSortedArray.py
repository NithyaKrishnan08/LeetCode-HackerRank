# Find First and Last Position of Element in Sorted Array
# Leetcode Problem 34: Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
'''

from typing import List

class Solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    n = len(nums)

    if n == 0:
      return [-1, -1]
    
    def searchFirst(nums, target):
      low, high = 0, n - 1
      first = -1

      while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
          first = mid
          high = mid - 1
        elif nums[mid] < target:
          low = mid + 1
        else:
          high = mid - 1
      
      return first
    
    def searchLast(nums, target):
      low, high = 0, n - 1
      last = -1

      while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
          last = mid
          low = mid + 1
        elif nums[mid] < target:
          low = mid + 1
        else:
          high = mid - 1
      
      return last
    
    first = searchFirst(nums, target)
    last = searchLast(nums, target)
    return [first, last]
    
if __name__ == '__main__':
  solver = Solution()
  print(solver.searchRange([5,7,7,8,8,10], 8)) # [3,4]
  print(solver.searchRange([5,7,7,8,8,10], 6)) # [-1,-1]
  print(solver.searchRange([], 0)) # [-1,-1]
  print(solver.searchRange([2,2], 2)) # [0,1]
  print(solver.searchRange([1], 1)) # [0,0]
