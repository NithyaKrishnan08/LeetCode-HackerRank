# Largest Divisible Subset
# https://leetcode.com/problems/largest-divisible-subset/
# LeetCode 368

'''
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.
'''
from typing import List

class Solution:
  # TC: O(n^2) + O(n log n) for sorting
  # SC: O(n)
  def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    nums.sort()
    n = len(nums)
    dp = [1] * (n) # dp[i] = length of LIS ending at index i
    parent = [-1] * (n) # parent[i] = index of previous element in LIS ending at index i

    max_len = 1
    last_index = 0 # index of the last element in the LIS

    for i in range(n):
      for prev_index in range(i):
        if (nums[i] % nums[prev_index] == 0) and dp[prev_index] + 1 > dp[i]:
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
    return lis

if __name__ == '__main__':
  print(Solution().largestDivisibleSubset(nums = [1,2,3]))
  print(Solution().largestDivisibleSubset(nums = [1,2,4,8]))