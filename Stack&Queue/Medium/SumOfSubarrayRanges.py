# Sum of Sub Array Ranges
# https://leetcode.com/problems/sum-of-subarray-ranges/description/
# Leetcode: 2104
# Difficulty: Medium

'''
You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
Example 2:

Input: nums = [1,3,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[3], range = 3 - 3 = 0
[3], range = 3 - 3 = 0
[1,3], range = 3 - 1 = 2
[3,3], range = 3 - 3 = 0
[1,3,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
Example 3:

Input: nums = [4,-2,-3,4,1]
Output: 59
Explanation: The sum of all subarray ranges of nums is 59.
 

Constraints:

1 <= nums.length <= 1000
-109 <= nums[i] <= 109
'''
from typing import List

class Solution:
  # Brute force solution
  # TC: O(N^2)
  # SC: O(1)
  def subArrayRanges1(self, nums: List[int]) -> int:
    n = len(nums)
    total_subArrayRange = 0

    for i in range(n):
      min_val = max_val = nums[i]
      for j in range(i, n):
        min_val = min(min_val, nums[j])
        max_val = max(max_val, nums[j])
        total_subArrayRange += (max_val - min_val)

    return total_subArrayRange
  
  # Better solution
  # TC: O(N^2)
  # SC: O(1)
  def subArrayRanges2(self, nums: List[int]) -> int:
    n = len(nums)
    total_subArrayRange = 0

    for i in range(n):
      for j in range(i + 1, n + 1):
        min_range = min(nums[i:j])
        max_range = max(nums[i:j])
        total_subArrayRange += (max_range - min_range)

    return total_subArrayRange
  
  # Optimal solution
  # TC: O(N)
  # SC: O(1)
  def subArrayRanges(self, nums: List[int]) -> int:
    n = len(nums)
    
    # Step 1: Calculate sum of subarray maximums
    def sum_subarray_max(nums):
      stack = []
      res = 0
      
      for i in range(n + 1):
        while stack and (i == n or nums[stack[-1]] < nums[i]):
          mid = stack.pop()
          left = stack[-1] if stack else -1
          right = i
          count = (mid - left) * (right - mid)
          res += nums[mid] * count
        stack.append(i)
      
      return res
    
    # Step 2: Calculate sum of subarray minimums
    def sum_subarray_min(nums):
      stack = []
      res = 0
      
      for i in range(n + 1):
        while stack and (i == n or nums[stack[-1]] > nums[i]):
          mid = stack.pop()
          left = stack[-1] if stack else -1
          right = i
          count = (mid - left) * (right - mid)
          res += nums[mid] * count
        stack.append(i)
      
      return res
    
    return sum_subarray_max(nums) - sum_subarray_min(nums)
   

if __name__ == "__main__":
  arr = [4,-2,-3,4,1]
  solution = Solution()
  result = solution.subArrayRanges1(arr)
  print(result)

    