# Number of Longest Increasing Subsequences
# https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/
# Leetcode 673

'''
Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.
 

Constraints:

1 <= nums.length <= 2000
-106 <= nums[i] <= 106
The answer is guaranteed to fit inside a 32-bit integer.
'''

from typing import List

class Solution:
  def findNumberOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [1] * n # LIS from left
    cnt = [1] * n # no. of LIS

    for i in range(n):
      for j in range(i):
        if nums[i] > nums[j]:
          if 1 + dp[j] > dp[i]:
            dp[i] = 1 + dp[j]
            cnt[i] = cnt[j]
          elif 1 + dp[j] == dp[i]:
            cnt[i] += cnt[j]

    lis = max(dp)
    lis_count = 0

    for i in range(n):
      if dp[i] == lis:
        lis_count += cnt[i]

    return lis_count
  
if __name__ == "__main__":
  sol = Solution()
  print(sol.findNumberOfLIS(nums = [1,3,5,4,7])) # 2
  print(sol.findNumberOfLIS(nums = [2,2,2,2,2])) # 5
        