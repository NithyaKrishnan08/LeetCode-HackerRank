# Find minimum number of coins
# This works for standard denomination - for better solution dynamic programming is preferred

'''
Problem Statement: Given a value V, if we want to make a change for V Rs, and we have an infinite supply of each of the denominations in Indian currency, i.e., we have an infinite supply of { 1, 2, 5, 10, 20, 50, 100, 500, 1000} valued coins/notes, what is the minimum number of coins and/or notes needed to make the change.

Examples:

Example 1:

Input: V = 70

Output: 2

Explaination: We need a 50 Rs note and a 20 Rs note.

Example 2:

Input: V = 121

Output: 3

Explaination: We need a 100 Rs note, a 20 Rs note and a 1 Rs coin.
'''

class Solution:
  def coinChange(self, coins, amount):
    if amount == 0:
      return []

    result = []
    n = len(coins)

    for i in range(n - 1, -1, -1):
      while amount >= coins[i]:
        amount -= coins[i]
        result.append(coins[i])
    
    return result
  
if __name__ == "__main__":
  coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
  amount = 49
  solution = Solution()
  result = solution.coinChange(coins, amount)
  print(result)
