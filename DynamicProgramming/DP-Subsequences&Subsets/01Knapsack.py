# 0/1 Knapsack Problem
# Recursion to Single Array Space Optimised Approach

'''
Given n items, each with a specific weight and value, and a knapsack with a capacity of W, the task is to put the items in the knapsack such that the sum of weights of the items <= W and the sum of values associated with them is maximized. 

Note: You can either place an item entirely in the bag or leave it out entirely. Also, each item is available in single quantity.

Examples :

Input: W = 4, val[] = [1, 2, 3], wt[] = [4, 5, 1] 
Output: 3
Explanation: Choose the last item, which weighs 1 unit and has a value of 3.
Input: W = 3, val[] = [1, 2, 3], wt[] = [4, 5, 6] 
Output: 0
Explanation: Every item has a weight exceeding the knapsack's capacity (3).
Input: W = 5, val[] = [10, 40, 30, 50], wt[] = [5, 4, 2, 3] 
Output: 80
Explanation: Choose the third item (value 30, weight 2) and the last item (value 50, weight 3) for a total value of 80.
Constraints:
2 ≤ val.size() = wt.size() ≤ 103
1 ≤ W ≤ 103
1 ≤ val[i] ≤ 103
1 ≤ wt[i] ≤ 103
'''
from typing import List

class Solution:
  # Recursion
  def maxValueByWeight0(self, W: int, val: List[int], wt: List[int]) -> int:
    n = len(val)

    def maxValue(i, w):
      # Base case
      if i == 0:
        return val[0] if wt[0] <= w else 0
      
      not_take = maxValue(i - 1, w)
      
      take = 0
      if wt[i] <= w:
        take = val[i] + maxValue(i - 1, w - wt[i])

      return max(take, not_take)

    return maxValue(n - 1, W)
  
  # Memoization
  def maxValueByWeight1(self, W: int, val: List[int], wt: List[int]) -> int:
    n = len(val)
    dp = [[-1] * (W + 1) for _ in range(n)]

    def maxValue(i, w):
      # Base case
      if i == 0:
        return val[0] if wt[0] <= w else 0
      
      if dp[i][w] != -1:
        return dp[i][w]
      
      not_take = maxValue(i - 1, w)
      
      take = 0
      if wt[i] <= w:
        take = val[i] + maxValue(i - 1, w - wt[i])

      dp[i][w] = max(take, not_take)
      return dp[i][w]

    return maxValue(n - 1, W)
  
  # Tabulation
  # Step 1: Base case
  # Step 2: Write loop for i and w
  # Step 3: Recurrence relation
  def maxValueByWeight2(self, W: int, val: List[int], wt: List[int]) -> int:
    n = len(val)
    dp = [[0] * (W + 1) for _ in range(n)]

    # Base case: If the weight of the first item is less than or equal to W, we can take it
    for w in range(W + 1):
      if wt[0] <= w:
        dp[0][w] = val[0]

    # Fill the dp table
    for i in range(1, n):
      for w in range(W + 1):
        not_take = dp[i - 1][w]

        take = 0
        if wt[i] <= w:
          take = val[i] + dp[i - 1][w - wt[i]]

        dp[i][w] = max(take, not_take)

    return dp[n - 1][W]
  
  # Space Optimized with Single Array
  def maxValueByWeight3(self, W: int, val: List[int], wt: List[int]) -> int:
    n = len(val)
    prev = [0] * (W + 1)

    # Base case: only item 0
    for w in range(wt[0], W + 1):
      prev[w] = val[0]

    # Process the rest of items
    for i in range(1, n):
      # Traverse weights in reverse to avoid overwriting dependencies
      for w in range(W,  wt[i] - 1, -1):
        prev[w] = max(prev[w], val[i] + prev[w - wt[i]])

    return prev[W]
  
if __name__ == "__main__":
  sol = Solution()
  print(sol.maxValueByWeight3(4, [1, 2, 3], [4, 5, 1]))  # Output: 3
  print(sol.maxValueByWeight3(3, [1, 2, 3], [4, 5, 6]))  # Output: 0
  print(sol.maxValueByWeight3(5, [10, 40, 30, 50], [5, 4, 2, 3]))  # Output: 80
    