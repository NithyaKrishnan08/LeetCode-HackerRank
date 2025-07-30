# Unbounded Knapsack Problem - Thief

'''
A thief wants to rob a store. He is carrying a bag of capacity W. The store has ‘n’ items of infinite supply. Its weight is given by the ‘wt’ array and its value by the ‘val’ array. He can either include an item in its knapsack or exclude it but can’t partially have it as a fraction. We need to find the maximum value of items that the thief can steal. He can take a single item any number of times he wants and put it in his knapsack.
'''

from typing import List

class Solution:
  # Recursion
  # TC: Exponential
  # SC: O(n) for recursion stack
  def maxValueByWeight0(self, W: int, val: List[int], wt: List[int]) -> int:
    n = len(val)

    def maxValue(i, w):
      # Base case
      if i == 0:
        return (w // wt[0]) * val[0] if wt[0] <= w else 0
      
      not_take = maxValue(i - 1, w)
      
      take = 0
      if wt[i] <= w:
        take = val[i] + maxValue(i, w - wt[i])

      return max(take, not_take)

    return maxValue(n - 1, W)
  
  # Memoization
  def maxValueByWeight1(self, W: int, val: List[int], wt: List[int]) -> int:
    n = len(val)
    dp = [[-1] * (W + 1) for _ in range(n)]

    def maxValue(i, w):
      # Base case
      if i == 0:
        return (w // wt[0]) * val[0] if wt[0] <= w else 0
      
      if dp[i][w] != -1:
        return dp[i][w]
      
      not_take = maxValue(i - 1, w)
      
      take = 0
      if wt[i] <= w:
        take = val[i] + maxValue(i, w - wt[i])

      dp[i][w] = max(take, not_take)
      return dp[i][w]

    return maxValue(n - 1, W)
  
  # Tabulation - Bottom Up - From 0 to n - 1
  # Step 1: Base case
  # Step 2: Write loop for i and w
  # Step 3: Recurrence relation
  def maxValueByWeight2(self, W: int, val: List[int], wt: List[int]) -> int:
    n = len(val)
    dp = [[0] * (W + 1) for _ in range(n)]

    # Base case: If the weight of the first item is less than or equal to W, we can take it
    for w in range(W + 1):
      if wt[0] <= w:
        dp[0][w] = (w // wt[0]) * val[0]

    # Fill the dp table
    for i in range(1, n):
      for w in range(W + 1):
        not_take = dp[i - 1][w]

        take = 0
        if wt[i] <= w:
          take = val[i] + dp[i][w - wt[i]]

        dp[i][w] = max(take, not_take)

    return dp[n - 1][W]
  
  # Space Optimized with Single Array
  def maxValueByWeight3(self, W: int, val: List[int], wt: List[int]) -> int:
    n = len(val)
    prev = [0] * (W + 1)

    # Base case: only item 0
    for w in range(wt[0], W + 1):
      prev[w] = (w // wt[0]) * val[0]

    # Process the rest of items
    for i in range(1, n):
      # Traverse weights in reverse to avoid overwriting dependencies
      for w in range(wt[i], W + 1):
        prev[w] = max(prev[w], val[i] + prev[w - wt[i]])

    return prev[W]
  
if __name__ == "__main__":
  sol = Solution()
  print(sol.maxValueByWeight3(10, [5, 11, 13], [2, 4, 6]))  # Output: 3
    