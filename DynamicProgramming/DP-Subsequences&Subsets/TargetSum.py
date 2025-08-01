# Target Sum Problem
# https://leetcode.com/problems/target-sum/description/

'''
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1
 

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
'''
from typing import List

class Solution:
  def findTargetSumWays(self, nums: List[int], target: int) -> int:
    total_sum = sum(nums)

    # Transform the problem
    if (target + total_sum) % 2 != 0 or abs(target) > total_sum:
      return 0

    subset_sum = (target + total_sum) // 2
    n = len(nums)

    dp = [[0 for _ in range(subset_sum + 1)] for _ in range(n)]

    # Base case
    if nums[0] == 0:
      dp[0][0] = 2  # pick or not pick zero
    else:
      dp[0][0] = 1  # don't pick anything = 0 sum
      if nums[0] <= subset_sum:
        dp[0][nums[0]] = 1  # pick first element

    for i in range(1, n):
      for t in range(subset_sum + 1):
        not_take = dp[i - 1][t]
        take = dp[i - 1][t - nums[i]] if nums[i] <= t else 0
        dp[i][t] = take + not_take

    return dp[n - 1][subset_sum]
  
sol = Solution()
print(sol.findTargetSumWays([0,0,0,0,1], 1)) 
