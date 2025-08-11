# Print Longest Increasing Subsequence - LIS
# https://leetcode.com/problems/longest-increasing-subsequence/description/
# LeetCode 300

'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
'''
from typing import List

class Solution:
  def printLIS(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [1] * (n) # dp[i] = length of LIS ending at index i
    parent = [-1] * (n) # parent[i] = index of previous element in LIS ending at index i

    max_len = 1
    last_index = 0 # index of the last element in the LIS

    for i in range(n):
      for prev_index in range(i):
        if nums[prev_index] < nums[i] and dp[prev_index] + 1 > dp[i]:
          dp[i] = 1 + dp[prev_index]
          parent[i] = prev_index

      if dp[i] > max_len:
        max_len = dp[i]
        last_index = i

    # Reconstruct the LIS
    lis = []
    while last_index != -1:
      lis.append(nums[last_index])
      last_index = parent[last_index]

    lis.reverse()
    print("Longest Increasing Subsequence:", lis)
  
if __name__ == '__main__':
  nums = [10,9,2,5,3,7,101,18]
  Solution().printLIS(nums = [10,9,2,5,3,7,101,18]) # [2, 5, 7, 101]
  Solution().printLIS(nums = [0,1,0,3,2,3])  # [0, 1, 2, 3]
  Solution().printLIS(nums = [7,7,7,7,7,7,7]) # [7]
