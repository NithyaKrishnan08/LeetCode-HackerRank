# Longest Increasing Subsequence - LIS
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
from bisect import bisect_left

class Solution:
  # Recursion
  # TC: O(2^n)
  # SC: O(n) for recursion stack

  # Step 1: Express everything in terms of (index, prevIndex)
  # Step 2: Try all possibilities and choose the best
  # Step 3: Take the max of all possibilities
  # Step 4: Base case
  # prev = -1 means no previous element
  def lengthOfLIS0(self, nums: List[int]) -> int:
    n = len(nums)

    def lis(i, prev_index):
      if i == n:
        return 0
      
      not_take = lis(i + 1, prev_index)
      
      take = 0
      if prev_index == -1 or nums[i] > nums[prev_index]:
        take = 1 + lis(i + 1, i) # Include current element

      length = max(take, not_take)

      return length

    return lis(0, -1)
  
  # Memoization
  # TC: O(n * n)
  # SC: O(n * n) + O(n) for recursion stack
  def lengthOfLIS1(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [[-1] * (n + 1) for _ in range(n)]

    def lis(i, prev_index):
      if i == n:
        return 0
      
      if dp[i][prev_index + 1] != -1:
        return dp[i][prev_index + 1]
      
      not_take = lis(i + 1, prev_index)
      
      take = 0
      if prev_index == -1 or nums[i] > nums[prev_index]:
        take = 1 + lis(i + 1, i) # Include current element

      dp[i][prev_index + 1] = max(take, not_take)

      return dp[i][prev_index + 1]

    return lis(0, -1)
  
  # Tabulation
  # TC: O(n * n)
  # SC: O(n * n)
  def lengthOfLIS2(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
      for prev_index in range(i - 1, -2, -1):
        not_take = dp[i + 1][prev_index + 1]

        take = 0
        if prev_index == -1 or nums[i] > nums[prev_index]:
          take = 1 + dp[i + 1][i + 1]

        dp[i][prev_index + 1] = max(take, not_take)

    return dp[0][0]
  
  # Space Optimized
  # TC: O(n * n)
  # SC: O(n)
  def lengthOfLIS3(self, nums: List[int]) -> int:
    n = len(nums)
    next_dp = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
      curr_dp = [0] * (n + 1)
      for prev_index in range(i - 1, -2, -1):
        not_take = next_dp[prev_index + 1]

        take = 0
        if prev_index == -1 or nums[i] > nums[prev_index]:
          take = 1 + next_dp[i + 1]

        curr_dp[prev_index + 1] = max(take, not_take)
      next_dp = curr_dp

    return next_dp[0]
  
  # Space Optimized
  # TC: O(n * n)
  # SC: O(n)
  def lengthOfLIS4(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [1] * (n)

    for i in range(n):
      for prev_index in range(i):
        if (nums[prev_index] < nums[i]) and 1 + dp[prev_index] > dp[i]:
          dp[i] = 1 + dp[prev_index]

    return max(dp)
  
  # Binary Search
  # TC: O(n * n)
  # SC: O(n)
  def lengthOfLIS5(self, nums: List[int]) -> int:
    sub = []

    for num in nums:
      i = bisect_left(sub, num) # Find the index to insert num in sub
      if i == len(sub):
        sub.append(num)
      else:
        sub[i] = num

    return len(sub)
  
if __name__ == '__main__':
  nums = [10,9,2,5,3,7,101,18]
  print(Solution().lengthOfLIS4(nums = [10,9,2,5,3,7,101,18]))  # 4
  print(Solution().lengthOfLIS4(nums = [0,1,0,3,2,3]))  # 4
  print(Solution().lengthOfLIS4(nums = [7,7,7,7,7,7,7]))  # 1
        