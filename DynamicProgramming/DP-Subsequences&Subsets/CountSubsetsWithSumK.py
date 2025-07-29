# Counts Subsets with Sum K
# https://leetcode.com/problems/subarray-sum-equals-k/description/

'''
Problem statement
You are given an array 'arr' of size 'n' containing positive integers and a target sum 'k'.

Find the number of ways of selecting the elements from the array such that the sum of chosen elements is equal to the target 'k'.

Since the number of ways can be very large, print it modulo 10 ^ 9 + 7.

Example:
Input: 'arr' = [1, 1, 4, 5]

Output: 3

Explanation: The possible ways are:
[1, 4]
[1, 4]
[5]
Hence the output will be 3. Please note that both 1 present in 'arr' are treated differently.
'''

from typing import List
MOD = 10**9 + 7

class Solution:
  # Recursive solution
  # TC: O(2^N)
  # SC: O(N)
  # Step 1: Express in terms of (idx, target)
  # Step 2: Explore possibilities of that idx: a[idx] - part of the subsequence & a[idx] - not part of the subsequence
  # Step 3: Return the count of subsequences that sum to target
  def subarraySum0(self, nums: List[int], k: int) -> int:
    def count(i, target):
      if i == 0:
        if target == 0 and nums[0] == 0:
          return 2  # Pick or not pick the zero
        if target == 0 or nums[0] == target:
          return 1
        return 0

      not_take = count(i - 1, target)
      take = count(i - 1, target - nums[i]) if nums[i] <= target else 0
      
      return take + not_take
    
    return count(len(nums) - 1, k)
  
  # Memoization solution
  # TC: O(2^N)
  # SC: O(N)
  def subarraySum1(self, nums: List[int], k: int) -> int:
    n = len(nums)
    total_sum = sum(abs(num) for num in nums) # Max possible absolute sum
    offset = total_sum  # Offset for negative indices
    dp = [[-1] * ( 2 * total_sum + 1) for _ in range(n)]

    def count(i, target):
      index = target + offset

      if index < 0 or index >= 2 * total_sum + 1:
        return 0
      
      # Base case for index 0
      if i == 0:
        base = 0
        if nums[0] == 0 and target == 0:
          return 2  # Pick or not pick the zero
        if target == 0 or target == nums[0]:
          return 1
        return 0
      
      if dp[i][index] != -1:
        return dp[i][index]

      not_take = count(i - 1, target)
      take = count(i - 1, target - nums[i])
      
      dp[i][index] = take + not_take
      return dp[i][index]
    
    return count(n - 1, k)
  
if __name__ == "__main__":
  sol = Solution()
  nums = [1, 1, 1]
  k = 2
  
  # Recursive solution
  # result = sol.subarraySum0(nums, k)
  # print(result)
  
  # Memoization solution
  result = sol.subarraySum1(nums, k)
  print(result)
  
  # Tabulation solution
  # result = sol.subarraySum2(nums, k)
  # print(result)