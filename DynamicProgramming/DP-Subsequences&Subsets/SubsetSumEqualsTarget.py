# Subset sum equals to target
# LeetCode 560. Subarray Sum Equals K

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
from collections import defaultdict

class Solution:
  # Step 1: Express (idx, target)
  # Step 2: Explre possibilities of that idx: a[idx] - part of the subsequence & a[idx] - not part of the subsequence
  def subarraySum0(self, nums: List[int], k: int) -> int:
    def count_from_index(start):
      if start == len(nums):
        return 0
      
      count = 0
      s = 0
      for end in range(start, len(nums)):
        s += nums[end]
        if s == k:
          count += 1
      return count + count_from_index(start + 1)
    return count_from_index(0)

if __name__ == "__main__":
  sol = Solution()
  nums = [1,1,1]
  k = 2

  # Recursive solution
  result = sol.subarraySum0(nums, k)
  print(result)
