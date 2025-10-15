# Longest Subarray with 0 Sum
# Difficulty: Medium

'''
Given an array arr[] consisting of both positive and negative integers, find the length of the longest subarray whose elements sum is zero.
A subarray is a contiguous part of an array, formed by selecting one or more consecutive elements while maintaining their original order.

Examples:

Input: arr[] = [15, -2, 2, -8, 1, 7, 10]
Output: 5
Explanation: The longest subarray with sum equals to 0 is [-2, 2, -8, 1, 7].

Input: arr[] = [1, 2, 3]
Output: 0
Explanation: There is no subarray with 0 sum.

Input:  arr[] = [1, 0, 3]
Output:  1
Explanation: The longest sub-array with sum equal to 0 is [0].
'''

from typing import List

class Solution:
  def NoOfLongestSubarray(self, nums: List[int]) -> int:
    n = len(nums)
    premap = {}
    prefix_sum, max_len = 0, 0

    for i in range(n):
      prefix_sum += nums[i]

      if prefix_sum in premap:
        max_len = max(max_len, i - premap[prefix_sum])

      if prefix_sum not in premap:
        premap[prefix_sum] = i

    return max_len
  
if __name__ == '__main__':
  sol = Solution()
  print(sol.NoOfLongestSubarray([15, -2, 2, -8, 1, 7, 10]))   # 5