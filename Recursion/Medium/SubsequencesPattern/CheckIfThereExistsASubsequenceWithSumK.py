# Check if there exists a subsequence with sum K
# Difficulty: Medium

'''
Problem Statement: Given an array nums and an integer k. Return true if there exist subsequences such that the sum of all elements in subsequences is equal to k else false.

Examples
Example 1:
Input : nums = [1, 2, 3, 4, 5] , k = 8
Output : Yes
Explanation : The subsequences like [1, 2, 5] , [1, 3, 4] , [3, 5] sum up to 8.

Example 2:
Input : nums = [4, 3, 9, 2] , k = 10
Output : No
Explanation : No subsequence can sum up to 10.
'''

from typing import List

class Solution:
  def checkSubsequenceWithSumK(self, nums: List[int], k: int) -> bool:
    def backtrack(idx, current_sum):
      if idx == len(nums):
        return current_sum == k

      # Include the current idx number
      include = backtrack(idx + 1, current_sum + nums[idx])
      if include:
        return True

      # Exclude the current idx number
      exclude = backtrack(idx + 1, current_sum)
      return exclude

    return backtrack(0, 0)
  
if __name__ == '__main__':
  sol = Solution()
  print(sol.checkSubsequenceWithSumK([1, 2, 3, 4, 5], 8))
  print(sol.checkSubsequenceWithSumK([4, 3, 9, 2], 10))