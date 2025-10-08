# Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/description/
# Difficulty: Medium

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
    prefix_sum, count = 0, 0
    prefix_map = {0: 1}

    for num in nums:
      prefix_sum += num

      remaining = prefix_sum - k
      if remaining in prefix_map:
        count += prefix_map[remaining]

      prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

    return count
  
if __name__ == '__main__':
  sol = Solution()
  print(sol.subarraySum(nums = [1,1,1], k = 2)) # 2
  print(sol.subarraySum(nums = [1,2,3], k = 3)) # 2
