# Best time to buy and sell stock III
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
# LeetCode 123

'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 105
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

    return buyorSell(0, 1, 2)  # Start with index 0, canBuy = True, and max_transactions = 2
  
  # Memoization
  # TC: O(n*2)
  # SC: O(n*2) + O(n) for recursion stack
  def maxProfit1(self, prices: List[int]) -> int:
    n = len(prices)
    dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]

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

    return buyorSell(0, 1, 2)
  
  # Tabulation
  # Step 1: Base case
  # Step 2: Write for i and canBuy loops
  # Step 3: Copy the recurrence
  # TC: O(n*2)
  # SC: O(n*2)
  def maxProfit2(self, prices: List[int]) -> int:
    n = len(prices)

    dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]
    
    for i in range(n - 1, -1, -1):
      for canBuy in range(2):
        for transactions_left in range(1, 3):
          if canBuy:
            buy = -prices[i] + dp[i + 1][0][transactions_left] # Buy
            not_buy = dp[i + 1][1][transactions_left]  # Do not buy
            dp[i][canBuy][transactions_left] = max(buy, not_buy)
          else:
            sell = prices[i] + dp[i + 1][1][transactions_left - 1]  # Sell
            not_sell = dp[i + 1][0][transactions_left]  # Do not sell
            dp[i][canBuy][transactions_left] = max(sell, not_sell)

    return dp[0][1][2]
  
if __name__ == '__main__':
  prices1 = [3,3,5,0,0,3,1,4]
  prices2 = [1,2,3,4,5]
  prices3 = [7,6,4,3,1]
  print(Solution().maxProfit2(prices1))  # 6
  print(Solution().maxProfit2(prices2))  # 4
  print(Solution().maxProfit2(prices3))  # 0