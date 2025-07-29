'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0
 
Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
'''

# Minimum no. of coins to make up the amount

# Memoization
# Time Complexity: O(N * amount)
# Space Complexity: O(N * amount) + O(N)

from typing import List

class Solution:
  # Recursion
  def coinChange0(self, coins: List[int], amount: int) -> int:
    n = len(coins)

    def minimumElementsUtil0(index, amount):
      if index == 0:
        if amount % coins[0] == 0:
          return amount // coins[0]
        else:
          return int(1e9)
      
      notTaken = minimumElementsUtil0(index - 1, amount)
      
      taken = int(1e9)
      if coins[index] <= amount:
        taken = 1 + minimumElementsUtil0(index, amount - coins[index])

      no_coins = min(taken, notTaken)
      return no_coins
    
    return minimumElementsUtil0(n - 1, amount)
  
  def minimumElementsUtil(self, coins, index, amount, dp):
    if index == 0:
      if amount % coins[0] == 0:
        return amount // coins[0]
      else:
        return int(1e9)
      
    if dp[index][amount] != -1:
      return dp[index][amount]
    
    notTaken = self.minimumElementsUtil(coins, index - 1, amount, dp)
    taken = int(1e9)

    if coins[index] <= amount:
      taken = 1 + self.minimumElementsUtil(coins, index, amount - coins[index], dp)

    dp[index][amount] = min(taken, notTaken)
    return dp[index][amount]

  def coinChange1(self, coins: List[int], amount: int) -> int:
    n = len(coins)
    dp = [[-1 for _ in range(amount + 1)] for i in range(n)]
    result = self.minimumElementsUtil(coins, n - 1, amount, dp)
    if result >= int(1e9):
      return -1
    
    return result
  
  # Tabulation
  # Time Complexity: O(N * amount)
  # Space Complexity: O(N * amount) + O(N)

  def coinChange2(self, coins: List[int], amount: int) -> int:
    n = len(coins)
    dp = [[0 for _ in range(amount + 1)] for _ in range(n)]
    
    for i in range(amount + 1):
      if i % coins[0] == 0:
        dp[0][i] = i // coins[0]
      else:
        dp[0][i] = int(1e9)

    
    for index in range(1, n):
      for amount in range(amount + 1):
        notTaken = dp[index - 1][amount]
        taken = int(1e9)

        if coins[index] <= amount:
          taken = 1 + dp[index][amount - coins[index]]

        dp[index][amount] = min(taken, notTaken)

    result = dp[n-1][amount]
    if result >= int(1e9):
      return -1
    
    return result

if __name__ == "__main__":
  coins = [1, 2, 5]
  amount = 11
  solution = Solution()

  print("Recursion method:")
  result1 = solution.coinChange0(coins, amount)
  print(f"Minimum no. to coins to make {amount}: {result1}")

  print("Memoization method:")
  result2 = solution.coinChange1(coins, amount)
  print(f"Minimum no. to coins to make {amount}: {result2}")

  print("Tabulation method:")
  result3 = solution.coinChange2(coins, amount)
  print(f"Minimum no. to coins to make {amount}: {result3}")

