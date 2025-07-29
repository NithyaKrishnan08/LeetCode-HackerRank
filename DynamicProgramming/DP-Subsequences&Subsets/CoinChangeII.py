# Coin Change II
# https://leetcode.com/problems/coin-change-ii/description/

'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

 

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1
 

Constraints:

1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000
'''
from typing import List

class Solution:
  # Recursion
  # TC: Exponential
  # SC: O(n) for recursion stack
  def change0(self, amount: int, coins: List[int]) -> int:
    def count(i: int, amount: int) -> int:
      if amount == 0:
        return 1
      if i < 0 or amount < 0:
        return 0
      
      not_take = count(i - 1, amount)

      take = 0
      if coins[i] <= amount:
        take = count(i, amount - coins[i])
      
      return take + not_take

    return count(len(coins) - 1, amount)
  
  # Memoization
  def change1(self, amount: int, coins: List[int]) -> int:
    n = len(coins)
    dp = [[-1] * (amount + 1) for _ in range(n)]

    def count(i: int, amount: int) -> int:
      if amount == 0:
        return 1
      if i < 0 or amount < 0:
        return 0
      
      if dp[i][amount] != -1:
        return dp[i][amount]
      
      not_take = count(i - 1, amount)

      take = 0
      if coins[i] <= amount:
        take = count(i, amount - coins[i])
      
      dp[i][amount] = take + not_take
      return dp[i][amount]

    return count(len(coins) - 1, amount)
  
  # Tabulation
  def change2(self, amount: int, coins: List[int]) -> int:
    n = len(coins)
    dp = [[0] * (amount + 1) for _ in range(n)]

    # Base case: There's 1 way to make amount 0 — pick nothing
    for i in range(n):
      dp[i][0] = 1

    # Fill first row (only using coins[0])
    for t in range(coins[0], amount + 1):
      if t % coins[0] == 0:
        dp[0][t] = 1

    # Fill the rest of the table
    for i in range(1, n):
      for t in range(1, amount + 1):
        not_take = dp[i - 1][t] # Not taking the coin
        take = dp[i][t - coins[i]] if coins[i] <= t else 0
        dp[i][t] = take + not_take
    
    return dp[n - 1][amount]
  
if __name__ == "__main__":
  sol = Solution()
  print(sol.change2(5, [1, 2, 5]))  # Output: 4
  print(sol.change2(3, [2]))         # Output: 0
  print(sol.change2(10, [10]))       # Output: 1