# Binary Search to find X in sorted array
# https://leetcode.com/problems/binary-search/description/
# Leetcode: 704
# Difficulty: Easy

'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
'''

from typing import List

class Solution:
  def search(self, nums: List[int], target: int) -> int:
    n = len(nums)
    left, right = 0, n - 1

    while left <= right:
      middle = (left + right) // 2

      if nums[middle] == target:
        return middle
      elif nums[middle] < target:
        left = middle + 1
      else:
        right = middle - 1

    return -1
  
if __name__ == '__main__':
  sol = Solution()
  print(sol.search(nums = [-1,0,3,5,9,12], target = 9)) # 4
  print(sol.search(nums = [-1,0,3,5,9,12], target = 2)) # -1
