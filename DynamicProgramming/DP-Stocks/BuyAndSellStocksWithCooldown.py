# Buy and Sell Stocks With Cooldown
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
# LeetCode 309

'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0
 

Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000
'''

from typing import List

class Solution:
  # Recursion
  # TC: O(2^n)
  # SC: O(n) for recursion stack

  # Step 1: Express everything in terms of (index, canBuy)
  # Step 2: Try all possibilities and choose the best
  # Step 3: Take the max of all possibilities
  # Step 4: Base case
  # 1 -> true and 0 -> False
  def maxProfit0(self, prices: List[int]) -> int:
    n = len(prices)

    def buyorSell(i, canBuy):
      if i >= n:
        return 0

      if canBuy:
        buy = -prices[i] + buyorSell(i + 1, 0)  # Buy
        not_buy = buyorSell(i + 1, 1)  # Do not buy
        profit = max(buy, not_buy)
      else:
        sell = prices[i] + buyorSell(i + 2, 1)  # Sell
        not_sell = buyorSell(i + 1, 0)  # Do not sell
        profit = max(sell, not_sell)

      return profit

    return buyorSell(0, 1)
  
  # Memoization
  # TC: O(n*2)
  # SC: O(n*2) + O(n) for recursion stack
  def maxProfit1(self, prices: List[int]) -> int:
    n = len(prices)
    dp = [[-1] * 2 for _ in range(n)]

    def buyorSell(i, canBuy):
      if i >= n:
        return 0
      
      if dp[i][canBuy] != -1:
        return dp[i][canBuy]

      if canBuy:
        buy = -prices[i] + buyorSell(i + 1, 0)  # Buy
        not_buy = buyorSell(i + 1, 1)  # Do not buy
        dp[i][canBuy] = max(buy, not_buy)
      else:
        sell = prices[i] + buyorSell(i + 2, 1)  # Sell
        not_sell = buyorSell(i + 1, 0)  # Do not sell
        dp[i][canBuy] = max(sell, not_sell)

      return dp[i][canBuy]

    return buyorSell(0, 1)
  
  # Tabulation
  # Step 1: Base case
  # Step 2: Write for i and canBuy loops
  # Step 3: Copy the recurrence
  # TC: O(n*2)
  # SC: O(n*2)
  def maxProfit2(self, prices: List[int]) -> int:
    n = len(prices)

    # dp[i][0] = max profit on day i when we cannot buy (i.e., we are holding stock)
    # dp[i][1] = max profit on day i when we can buy
    dp = [[0] * 2 for _ in range(n + 2)]

    # Base case: at day n (after last day), profit is 0 regardless of canBuy
    for canBuy in range(2):
      dp[n][canBuy] = 0
    
    for i in range(n - 1, -1, -1):
      buy = -prices[i] + dp[i + 1][0] # Buy
      not_buy = dp[i + 1][1]  # Do not buy
      dp[i][1] = max(buy, not_buy)

      sell = prices[i] + dp[i + 2][1]  # Sell
      not_sell = dp[i + 1][0]  # Do not sell
      dp[i][0] = max(sell, not_sell)

    return dp[0][1]
  
  # Space Optimization
  # Step 1: Base case
  # Step 2: Write for i and canBuy loops
  # Step 3: Copy the recurrence
  # TC: O(n*2)
  # SC: O(1)
  def maxProfit3(self, prices: List[int]) -> int:
    n = len(prices)

    # prev and curr hold
    prev = [0, 0] # dp[i + 1]
    after = [0, 0] # dp[i]
    
    for i in range(n - 1, -1, -1):
      curr = [0, 0]

      buy = -prices[i] + prev[0] # Buy
      not_buy = prev[1]  # Do not buy
      curr[1] = max(buy, not_buy)

      sell = prices[i] + after[1]  # Sell
      not_sell = prev[0]  # Do not sell
      curr[0] = max(sell, not_sell)
      
      after = prev[:]
      prev = curr[:]

    return prev[1]
  
if __name__ == '__main__':
  print(Solution().maxProfit3(prices = [1,2,3,0,2]))  # 3
  print(Solution().maxProfit3(prices = [1]))  # 0