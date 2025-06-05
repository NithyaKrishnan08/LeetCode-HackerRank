# Subarray Sum Equals K

'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
'''
from typing import List

class Solution:
  def subarraySum(self, nums: List[int], k: int) -> int:
    n = len(nums)
    sub_arr_count = 0
    for i in range(n):
      sum = 0
      for j in range(i, n):
        sum += nums[j]
        if sum == k:
          sub_arr_count += 1
        elif sum > k:
          sum = 0
          break

    return sub_arr_count