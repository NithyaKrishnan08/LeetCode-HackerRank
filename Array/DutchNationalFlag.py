# Dutch National Flag algorithm
# Sort Colors

'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:

Input: nums = [2,0,1]
Output: [0,1,2] 

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
'''
from typing import List

class Solution:
  # Time complexity: O(2n)
  # Space complexity: O(1)
  # Two-pass algorithm
  def sortColorsBetter(self, nums: List[int]) -> None:
    count0, count1, count2 = 0, 0, 0
    for n in nums:
      if n == 0:
        count0 += 1
      elif n == 1:
        count1 += 1
      else:
        count2 += 1

    for i in range(len(nums)):
      if i < count0:
        nums[i] = 0
      elif i < count0 + count1:
        nums[i] = 1
      else:
        nums[i] = 2

    return nums
  
  # Dutch National Flag algorithm
  # Time complexity: O(n)
  # Space complexity: O(1)
  # [0 -- low - 1] -> 0s
  # [low -- mid - 1] -> 1s
  # [mid -- high] -> unknown (random nums in unsorted order)
  # [high + 1 -- n - 1] -> 2s
  def sortColors(self, nums: List[int]) -> None:
    n = len(nums)
    low, mid, high = 0, 0, n - 1

    while mid <= high:
      if nums[mid] == 0:
        nums[low], nums[mid] = nums[mid], nums[low]
        low += 1
        mid += 1
      elif nums[mid] == 1:
        mid += 1
      else:
        nums[mid], nums[high] = nums[high], nums[mid]
        high -= 1

    return nums
  
if __name__ == '__main__':
  solver = Solution()
  print(solver.sortColors([2,0,2,1,1,0]))
  print(solver.sortColors([2,0,1]))
  print(solver.sortColors([0]))
  print(solver.sortColors([1]))
  print(solver.sortColors([2]))
  print(solver.sortColors([1,2,0]))
  print(solver.sortColors([1,1,1,1,1,1,1,1,1,1]))
        