# Rod cutting Problem

'''
Given a rod of length n inches and an array price[]. price[i] denotes the value of a piece of length i. The task is to determine the maximum value obtainable by cutting up the rod and selling the pieces.

Note: price[] is 1-indexed array.

Input: price[] =  [1, 5, 8, 9, 10, 17, 17, 20]
Output: 22
Explanation:  The maximum obtainable value is 22 by cutting in two pieces of lengths 2 and 6, i.e., 5 + 17 = 22.

Input : price[] =  [3, 5, 8, 9, 10, 17, 17, 20]
Output : 24
Explanation : The maximum obtainable value is 24 by cutting the rod into 8 pieces of length 1, i.e, 8*price[1]= 8*3 = 24.

Input : price[] =  [3]
Output : 3
Explanation: There is only 1 way to pick a piece of length 1.
'''

from typing import List

class Solution:
  # Recursion
  # TC: Exponential
  # SC: O(n) for recursion stack
  def cutRod0(self, price: List[int]) -> int:
    n = len(price)

    def max_price(i, n):
      if i == 0:
        return n * price[0]
      
      not_take = max_price(i - 1, n)
      
      take = 0
      rod_length = i + 1
      if rod_length <= n:
        take = price[i] + max_price(i, n - rod_length)
      
      return max(take, not_take)
    
    return max_price(len(price) - 1, n)
  
  # Memoization
  # TC: O(n * (n + 1))
  # SC: O(n * n) + O(target)
  def cutRod1(self, price: List[int]) -> int:
    n = len(price)
    dp = [[-1] * (n + 1) for _ in range(n)]

    def max_price(i, n):
      if i == 0:
        return n * price[0]
      
      if dp[i][n] != -1:
        return dp[i][n]
      
      not_take = max_price(i - 1, n)
      
      take = 0
      rod_length = i + 1
      if rod_length <= n:
        take = price[i] + max_price(i, n - rod_length)
      
      dp[i][n] = max(take, not_take)
      return dp[i][n]
    
    return max_price(len(price) - 1, n)
  
  # Tabulation - Bottom Up - From 0 to n - 1
  # TC: O(n^2)
  # SC: O(n^2)
  def cutRod2(self, price: List[int]) -> int:
    n = len(price)
    dp = [[0] * (n + 1) for _ in range(n)]

    for j in range(n + 1):
      dp[0][j] = j * price[0]

    for i in range(1, n):
      rod_length = i + 1
      for j in range(n + 1):
        not_take = dp[i - 1][j]
        
        take = 0
        if rod_length <= j:
          take = price[i] + dp[i][j - rod_length]
        
        dp[i][j] = max(take, not_take)
    
    return dp[n - 1][n]
  
  # Space Optimization
  # TC: O(n^2)
  # SC: O(n)
  def cutRod3(self, price: List[int]) -> int:
    n = len(price)
    prev = [0] * (n + 1)

    for j in range(n + 1):
      prev[j] = j * price[0]

    for i in range(1, n):
      rod_length = i + 1
      for j in range(n + 1):
        not_take = prev[j]
        
        take = 0
        if rod_length <= j:
          take = price[i] + prev[j - rod_length]
        
        prev[j] = max(take, not_take)
    
    return prev[n]
  
if __name__ == "__main__":
  price =  [1, 5, 8, 9, 10, 17, 17, 20]
  sol = Solution()
  print(sol.cutRod3(price))  # Output: 22