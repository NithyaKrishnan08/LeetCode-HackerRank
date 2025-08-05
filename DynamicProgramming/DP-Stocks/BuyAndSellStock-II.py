# Best time to buy and sell stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
# LeetCode 122

'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104
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
      if i == n:
        return 0

      if canBuy:
        buy = -prices[i] + buyorSell(i + 1, 0)  # Buy
        not_buy = buyorSell(i + 1, 1)  # Do not buy
        profit = max(buy, not_buy)
      else:
        sell = prices[i] + buyorSell(i + 1, 1)  # Sell
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
      if i == n:
        return 0
      
      if dp[i][canBuy] != -1:
        return dp[i][canBuy]

      if canBuy:
        buy = -prices[i] + buyorSell(i + 1, 0)  # Buy
        not_buy = buyorSell(i + 1, 1)  # Do not buy
        dp[i][canBuy] = max(buy, not_buy)
      else:
        sell = prices[i] + buyorSell(i + 1, 1)  # Sell
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
    dp = [[0] * 2 for _ in range(n + 1)]

    # Base case: at day n (after last day), profit is 0 regardless of canBuy
    for canBuy in range(2):
      dp[n][canBuy] = 0
    
    for i in range(n - 1, -1, -1):
      buy = -prices[i] + dp[i + 1][0] # Buy
      not_buy = dp[i + 1][1]  # Do not buy
      dp[i][1] = max(buy, not_buy)

      sell = prices[i] + dp[i + 1][1]  # Sell
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
    curr = [0, 0] # dp[i]
    
    for i in range(n - 1, -1, -1):
      buy = -prices[i] + prev[0] # Buy
      not_buy = prev[1]  # Do not buy
      curr[1] = max(buy, not_buy)

      sell = prices[i] + prev[1]  # Sell
      not_sell = prev[0]  # Do not sell
      curr[0] = max(sell, not_sell)
      
      prev = curr[:]

    return prev[1]
  
if __name__ == '__main__':
  prices = [7,1,5,3,6,4]
  print(Solution().maxProfit3(prices))  # 7