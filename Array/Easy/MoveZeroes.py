# Move Zeroes
# https://leetcode.com/problems/move-zeroes/description/
# Difficulty: Easy

'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
'''

from typing import List

class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
    n = len(nums)
    j = 0 # Pointer for the place to put the next non-zero element

    for i in range(n):
      if nums[i] != 0:
        if i != j:
          nums[i], nums[j] = nums[j], nums[i]
        j += 1

if __name__ == '__main__':
  solver = Solution()
  nums = [0,1,0,3,12]
  solver.moveZeroes(nums)
  print(nums)  # [1,3,12,0,0]
  
  nums = [0]
  solver.moveZeroes(nums)
  print(nums)  # [0]
  
  nums = [1,0,1]
  solver.moveZeroes(nums)
  print(nums)  # [1,1,0]
  
  nums = [4,2,4,0,0,3,0,5,1,0]
  solver.moveZeroes(nums)
  print(nums)  # [4,2,4,3,5,1,0,0,0,0]