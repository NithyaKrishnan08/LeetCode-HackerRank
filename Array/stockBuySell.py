'''
Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Examples:

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and 
sell on day 5 (price = 6), profit = 6-1 = 5.

Note: That buying on day 2 and selling on day 1 
is not allowed because you must buy before 
you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are 
done and the max profit = 0.
'''

#  Brute Force Solution
def sellBuyStock1(prices):
  maxProfit = 0
  n = len(prices)
  # min_price = float('inf')

  for i in range(n):
    for j in range(i+1, n):
      if prices[j] > prices[i]:
        maxProfit = max(prices[j] - prices[i], maxProfit)

  return maxProfit

if __name__ == "__main__":
  arr = [7, 1, 5, 3, 6, 4]
  maxPro = sellBuyStock1(arr)
  print("brute Force Solution: ")
  print("Max profit is: ", maxPro)

# Optimal Solution
def sellBuyStock2(prices):
  maxProfit = 0
  n = len(prices)
  min_price = float('inf')

  for i in range(n):
    min_price = min(min_price, prices[i])
    maxProfit = max(prices[i] - min_price, maxProfit)

  return maxProfit

if __name__ == "__main__":
  arr = [7, 1, 5, 3, 6, 4]
  maxPro = sellBuyStock2(arr)
  print("Optimal Solution: ")
  print("Max profit is: ", maxPro)