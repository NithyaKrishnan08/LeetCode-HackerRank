# Count all subsequences with sum K
# Difficulty: Hard

'''
Problem Statement: Given an array nums and an integer k.Return the number of non-empty subsequences of nums such that the sum of all elements in the subsequence is equal to k.

Examples
Example 1:
Input : nums = [4, 9, 2, 5, 1] , k = 10
Output : 2
Explanation : The possible subsets with sum k are [9, 1] , [4, 5, 1].

Example 2:
Input : nums = [4, 2, 10, 5, 1, 3] , k = 5
Output : 3
Explanation : The possible subsets with sum k are [4, 1] , [2, 3] , [5].
'''
from typing import List

class Solution:
  def printSubsequencesWithSumK(self, nums: List[int], k: int) -> List[List[int]]:
    def backtrack(idx, path, arr, result):
      if idx == len(arr):
        if path and sum(path) == k:
          result.append(path[:])
        return
        
      # Include the current idx number
      path.append(arr[idx])
      backtrack(idx + 1, path, arr, result)

      # Exclude the current idx number
      path.pop()
      backtrack(idx + 1, path, arr, result)

    answer = []
    backtrack(0, [], nums, answer)
    return answer
  
  def countSubsequencesWithSumK(self, nums: List[int], k: int) -> List[List[int]]:
    def backtrack(idx, current_sum):
      if idx == len(nums):
        if current_sum == k:
          return 1
        else:
          return 0

      return backtrack(idx + 1, current_sum + nums[idx]) + backtrack(idx + 1, current_sum)

    return backtrack(0, 0)
  

if __name__ == '__main__':
  sol = Solution()
  print(sol.printSubsequencesWithSumK([4, 9, 2, 5, 1], 10))
  print(sol.countSubsequencesWithSumK([4, 9, 2, 5, 1], 10))
  