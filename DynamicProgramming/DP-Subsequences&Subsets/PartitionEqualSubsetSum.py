# Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/description/

'''
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
'''
from typing import List
from collections import defaultdict

class Solution:
  # Step 1: Express (idx, target)
  # Step 2: Explre possibilities of that idx: a[idx] - part of the subsequence & a[idx] - not part of the subsequence
  # TC: O(2^N)
  # SC: O(N)
  def canPartition0(self, nums: List[int]) -> bool:
    total_sum = sum(nums)

    if total_sum % 2 != 0:
      return False
    
    target = total_sum // 2

    def count(i, k):
      if k == 0:
        return True
      if i < 0 or k < 0:
        return False
      
      not_take = count(i - 1, k)
      take = count(i - 1, k - nums[i]) if nums[i] <= k else False
      
      return take or not_take
    
    return count(len(nums) - 1, target)

  # Memoization approach
  # TC: O(n * k)
  # SC: O(n * k) + O(n) for recursion stack
  def canPartition1(self, nums: List[int]) -> bool:
    n = len(nums)
    total_sum = sum(nums)

    if total_sum % 2 != 0:
      return False
    
    k = total_sum // 2

    dp = [[-1 for _ in range(k + 1)] for _ in range(n)]

    def count(i, target):
      if target == 0:
        return True
      if i < 0 or target < 0:
        return False
      
      if dp[i][target] != -1:
        return dp[i][target]
      
      not_take = count(i - 1, target)
      take = count(i - 1, target - nums[i]) if nums[i] <= target else False
      
      dp[i][target] = take or not_take
      return dp[i][target]
    
    return count(n - 1, k)
  
  # Tabulation approach
  # TC: O(n * k)
  # SC: O(n * k)
  def canPartition2(self, nums: List[int]) -> bool:
    n = len(nums)
    total_sum = sum(nums)

    if total_sum % 2 != 0:
      return False
    
    k = total_sum // 2

    dp = [[False for _ in range(k + 1)] for _ in range(n)]

    # Target = 0 is always true
    for i in range(n):
      dp[i][0] = True
    # If first element is equal to target, then it is true
    if nums[0] <= k:
      dp[0][nums[0]] = True

    # Fill the dp table
    for i in range(1, n):
      for target in range(1, k + 1):
        not_take = dp[i - 1][target]
        take = dp[i - 1][target - nums[i]] if nums[i] <= target else False
        
        dp[i][target] = take or not_take

    return dp[n - 1][k]

if __name__ == "__main__":
  sol = Solution()
  nums = [1,5,11,5]

  # Recursive solution
  # result = sol.canPartition0(nums)
  # print(result)

  # Memoization solution
  # result = sol.canPartition1(nums)
  # print(result)

  # Memoization solution
  result = sol.canPartition2(nums)
  print(result)