# Burst Balloons
# https://leetcode.com/problems/burst-balloons/description/
# Leetcode: 312

'''
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

 

Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
Example 2:

Input: nums = [1,5]
Output: 10
 

Constraints:

n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100
'''
from typing import List

class Solution:
  # Recursion
  # TC: Exponential
  # SC: O(n) - recursive stack space
  def maxCoins0(self, nums: List[int]) -> int:
    n = len(nums)
    nums = [1] + nums + [1]

    def calculate_max_coins(i, j):
      if i > j:
        return 0
      
      max_coins = float('-inf')
      for k in range(i, j + 1):
        no_coins = nums[i - 1] * nums[k] * nums[j + 1] + calculate_max_coins(i, k - 1) + calculate_max_coins(k + 1, j)
        max_coins = max(max_coins, no_coins)

      return max_coins
      
    return calculate_max_coins(1, n)
  
  # Memoization
  # TC: O(n^2 * n) -> O(n^3)
  # SC: O(n^2) + O(n) -> Auxillary Stack Space
  def maxCoins1(self, nums: List[int]) -> int:
    n = len(nums)
    nums = [1] + nums + [1]
    dp = [[-1] * (n + 2) for _ in range(n + 2)]

    def calculate_max_coins(i, j):
      if i > j:
        return 0
      
      if dp[i][j] != -1:
        return dp[i][j]
      
      max_coins = float('-inf')

      for k in range(i, j + 1):
        no_coins = nums[i - 1] * nums[k] * nums[j + 1] + calculate_max_coins(i, k - 1) + calculate_max_coins(k + 1, j)
        max_coins = max(max_coins, no_coins)

      dp[i][j] = max_coins
      return dp[i][j]
      
    return calculate_max_coins(1, n)
  
  # Tabulation
  # Step 1: Base case
  # Step 2: Changing parameters
  # Step 3: Recurrence
  # TC: O(n^2 * n) -> O(n^3)
  # SC: O(n^2)
  def maxCoins2(self, nums: List[int]) -> int:
    n = len(nums)
    nums = [1] + nums + [1]
    dp = [[0] * (n + 2) for _ in range(n + 2)]

    for length in range(1, n + 1):
      for i in range(1, n - length + 2):
        j = i + length - 1

        for k in range(i, j + 1):
          no_coins = nums[i - 1] * nums[k] * nums[j + 1] + dp[i][k - 1]+ dp[k + 1][j]
          dp[i][j] = max(dp[i][j], no_coins)

    return dp[1][n]
  
if __name__ == "__main__":
  sol = Solution()
  print(sol.maxCoins2(nums=[3,1,5,8]))
  print(sol.maxCoins2(nums=[1,5]))