# Best time to buy and sell stock IV
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/
# LeetCode 188

'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
 

Constraints:

1 <= k <= 100
1 <= prices.length <= 1000
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
  def maxProfit0(self, k: int, prices: List[int]) -> int:
    n = len(prices)

    def buyorSell(i, canBuy, transactions_left):
      if transactions_left == 0 or i == n:
        return 0

      if canBuy:
        buy = -prices[i] + buyorSell(i + 1, 0, transactions_left)  # Buy
        not_buy = buyorSell(i + 1, 1, transactions_left)  # Do not buy
        profit = max(buy, not_buy)
      else:
        sell = prices[i] + buyorSell(i + 1, 1, transactions_left - 1)  # Sell
        not_sell = buyorSell(i + 1, 0, transactions_left)  # Do not sell
        profit = max(sell, not_sell)

      return profit

    return buyorSell(0, 1, k)  # Start with index 0, canBuy = True, and max_transactions = 2
  
  # Memoization
  # TC: O(n*2)
  # SC: O(n*2) + O(n) for recursion stack
  def maxProfit1(self, k: int, prices: List[int]) -> int:
    n = len(prices)
    dp = [[[-1 for _ in range(k + 1)] for _ in range(2)] for _ in range(n)]

    def buyorSell(i, canBuy, transactions_left):
      if transactions_left == 0 or i == n:
        return 0
      
      if dp[i][canBuy][transactions_left] != -1:
        return dp[i][canBuy][transactions_left]

      if canBuy:
        buy = -prices[i] + buyorSell(i + 1, 0, transactions_left)  # Buy
        not_buy = buyorSell(i + 1, 1, transactions_left)  # Do not buy
        dp[i][canBuy][transactions_left] = max(buy, not_buy)
      else:
        sell = prices[i] + buyorSell(i + 1, 1, transactions_left - 1)  # Sell
        not_sell = buyorSell(i + 1, 0, transactions_left)  # Do not sell
        dp[i][canBuy][transactions_left] = max(sell, not_sell)

      return dp[i][canBuy][transactions_left]

    return buyorSell(0, 1, k)
  
  # Tabulation
  # Step 1: Base case
  # Step 2: Write for i and canBuy loops
  # Step 3: Copy the recurrence
  # TC: O(n*2)
  # SC: O(n*2)
  def maxProfit2(self, k: int, prices: List[int]) -> int:
    n = len(prices)

    dp = [[[0 for _ in range(k + 1)] for _ in range(2)] for _ in range(n + 1)]
    
    for i in range(n - 1, -1, -1):
      for canBuy in range(2):
        for transactions_left in range(1, k + 1):
          if canBuy:
            buy = -prices[i] + dp[i + 1][0][transactions_left] # Buy
            not_buy = dp[i + 1][1][transactions_left]  # Do not buy
            dp[i][canBuy][transactions_left] = max(buy, not_buy)
          else:
            sell = prices[i] + dp[i + 1][1][transactions_left - 1]  # Sell
            not_sell = dp[i + 1][0][transactions_left]  # Do not sell
            dp[i][canBuy][transactions_left] = max(sell, not_sell)

    return dp[0][1][k]
  
if __name__ == '__main__':
  sol = Solution()
  print(sol.maxProfit2(k = 2, prices = [2,4,1]))  # 2
  print(sol.maxProfit2(k = 2, prices = [3,2,6,5,0,3]))  # 7