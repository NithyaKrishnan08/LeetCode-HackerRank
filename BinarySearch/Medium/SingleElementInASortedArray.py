# Single Element in a Sorted Array
# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
# Leetcode: 540
# Difficulty: Medium

'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10

Constraints:
1 <= nums.length <= 105
0 <= nums[i] <= 105
'''

from typing import List
from collections import Counter

class Solution:
  def singleNonDuplicate(self, nums: List[int]) -> int:
    n = len(nums)
    low, high = 0, n - 1

    while low < high:
      mid = (low + high) // 2
      
      # Ensure mid is even (pairs start at even indices)
      if mid % 2 == 1:
        mid -= 1
      
      # Compare mid with next element
      if nums[mid] == nums[mid + 1]:
        low = mid + 2
      else:
        high = mid

    return nums[low]
      
  def singleNonDuplicateBrute(self, nums: List[int]) -> int:
    nums_map = Counter(nums)
    for item, val in nums_map.items():
      if val == 1:
        return item
      

if __name__ == '__main__':
  sol = Solution()
  print(sol.singleNonDuplicate(nums = [1,1,2,3,3,4,4,8,8])) # 2
  print(sol.singleNonDuplicate(nums = [3,3,7,7,10,11,11])) # 10
