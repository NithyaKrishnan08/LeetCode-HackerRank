# Subset Sum II
# https://leetcode.com/problems/subsets-ii/description/
# Leetcode Problem 90: Subsets II


'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

'''
from typing import List

class Solution:
  # TC: O(2^N), SC: O(N)
  def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    result = []

    def backtrack(start, path):
      result.append(path[:])
      
      for i in range(start, n):
        if i > start and nums[i] == nums[i - 1]:
          continue

        path.append(nums[i])
        backtrack(i + 1, path[:])  # Allow the same element to be picked again
        path.pop()

    backtrack(0, [])
    return result
  
if __name__ == "__main__":
  sol = Solution()
  nums = [1,2,2]
  print(sol.subsetsWithDup(nums))  # Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
  
  nums = [0]
  print(sol.subsetsWithDup(nums))  # Output: [[],[0]]

        