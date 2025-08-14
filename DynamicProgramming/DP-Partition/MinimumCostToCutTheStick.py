# Minimum Cost to Cut the Stick
# https://leetcode.com/problems/minimum-cost-to-cut-a-stick/description/
# Leetcode 1547

'''


Code

Testcase

Test Result
Test Result
1547. Minimum Cost to Cut a Stick
Hard

Topics
premium lock icon
Companies

Hint
Given a wooden stick of length n units. The stick is labelled from 0 to n. For example, a stick of length 6 is labelled as follows:


Given an integer array cuts where cuts[i] denotes a position you should perform a cut at.

You should perform the cuts in order, you can change the order of the cuts as you wish.

The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts. When you cut a stick, it will be split into two smaller sticks (i.e. the sum of their lengths is the length of the stick before the cut). Please refer to the first example for a better explanation.

Return the minimum total cost of the cuts.

 

Example 1:


Input: n = 7, cuts = [1,3,4,5]
Output: 16
Explanation: Using cuts order = [1, 3, 4, 5] as in the input leads to the following scenario:

The first cut is done to a rod of length 7 so the cost is 7. The second cut is done to a rod of length 6 (i.e. the second part of the first cut), the third is done to a rod of length 4 and the last cut is to a rod of length 3. The total cost is 7 + 6 + 4 + 3 = 20.
Rearranging the cuts to be [3, 5, 1, 4] for example will lead to a scenario with total cost = 16 (as shown in the example photo 7 + 4 + 3 + 2 = 16).
Example 2:

Input: n = 9, cuts = [5,6,1,4,2]
Output: 22
Explanation: If you try the given cuts ordering the cost will be 25.
There are much ordering with total cost <= 25, for example, the order [4, 6, 5, 2, 1] has total cost = 22 which is the minimum possible.
 

Constraints:

2 <= n <= 106
1 <= cuts.length <= min(n - 1, 100)
1 <= cuts[i] <= n - 1
All the integers in cuts array are distinct.
'''
# Cost is length of the stick in which the index is located

from typing import List

class Solution:
  # Recursion
  # TC: Exponential -> O(2^m)
  # SC: O(m) - recursive stack space
  def minCost0(self, n: int, cuts: List[int]) -> int:
    cuts = [0] + sorted(cuts) + [n]
    c = len(cuts)

    def calculate_cost(i, j):
      if i > j:
        return 0
      
      min_cost = float('inf')
      for idx in range(i, j + 1):
        cost = cuts[j + 1] - cuts[i - 1] + calculate_cost(i, idx - 1) + calculate_cost(idx + 1, j)
        min_cost = min(min_cost, cost)

      return min_cost

    return calculate_cost(1, c - 2)
  
  # Memoization
  # TC: O(m^2)
  # SC: O(m^2)
  def minCost1(self, n: int, cuts: List[int]) -> int:
    cuts = [0] + sorted(cuts) + [n]
    m = len(cuts)

    dp = [[-1] * m for _ in range(m)]

    def calculate_cost(i, j):
      if i > j:
        return 0
      
      if dp[i][j] != -1:
        return dp[i][j]
      
      min_cost = float('inf')

      for idx in range(i, j + 1):
        cost = cuts[j + 1] - cuts[i - 1] + calculate_cost(i, idx - 1) + calculate_cost(idx + 1, j)
        min_cost = min(min_cost, cost)

      dp[i][j] = min_cost
      return dp[i][j]

    return calculate_cost(1, m - 2)
  
  # Tabulation
  # TC: O(m^2)
  # SC: O(m^2)
  def minCost2(self, n: int, cuts: List[int]) -> int:
    cuts = [0] + sorted(cuts) + [n]
    m = len(cuts)

    dp = [[0] * m for _ in range(m)]

    for i in range(m - 2, 0, -1):
      for j in range(i, m - 1):
        if i > j:
          return 0
        
        min_cost = float('inf')

        for idx in range(i, j + 1):
          cost = cuts[j + 1] - cuts[i - 1] + dp[i][idx - 1] + dp[idx + 1][j]
          min_cost = min(min_cost, cost)

        dp[i][j] = 0 if min_cost == float('inf') else min_cost

    return dp[1][m - 2]
  
if __name__ == "__main__":
  sol = Solution()
  print(sol.minCost2(7, [1, 3, 4, 5]))  # 16
  print(sol.minCost2(9, [5, 6, 1, 4, 2]))  # 22
        