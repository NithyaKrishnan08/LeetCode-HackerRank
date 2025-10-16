# Search Insert Position
# https://leetcode.com/problems/search-insert-position/description/
# Leetcode: 35
# Difficulty: Easy

'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
'''
from typing import List

class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    n = len(nums)
    left, right = 0, n - 1

    while left <= right:
      middle = (left + right) // 2

      if nums[middle] == target:
        return middle
      elif nums[middle] > target:
        right = middle - 1
      else:
        left = middle + 1

    return left
  
if __name__ == '__main__':
  sol = Solution()
  print(sol.searchInsert(nums = [1,3,5,6], target = 5)) # 2
  print(sol.searchInsert([1,3,5,6], 2))  # Output: 1
  print(sol.searchInsert([1,3,5,6], 7))  # Output: 4
  print(sol.searchInsert([1,3,5,6], 0))  # Output: 0