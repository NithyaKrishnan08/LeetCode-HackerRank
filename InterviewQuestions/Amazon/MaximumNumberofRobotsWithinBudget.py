# Maximum Number of Robots Within Budget
# https://leetcode.com/problems/maximum-number-of-robots-within-budget/
# Leetcode Problem 2398: Maximum Number of Robots Within Budget

'''
You have n robots. You are given two 0-indexed integer arrays, chargeTimes and runningCosts, both of length n. The ith robot costs chargeTimes[i] units to charge and costs runningCosts[i] units to run. You are also given an integer budget.

The total cost of running k chosen robots is equal to max(chargeTimes) + k * sum(runningCosts), where max(chargeTimes) is the largest charge cost among the k robots and sum(runningCosts) is the sum of running costs among the k robots.

Return the maximum number of consecutive robots you can run such that the total cost does not exceed budget.

 

Example 1:

Input: chargeTimes = [3,6,1,3,4], runningCosts = [2,1,3,4,5], budget = 25
Output: 3
Explanation: 
It is possible to run all individual and consecutive pairs of robots within budget.
To obtain answer 3, consider the first 3 robots. The total cost will be max(3,6,1) + 3 * sum(2,1,3) = 6 + 3 * 6 = 24 which is less than 25.
It can be shown that it is not possible to run more than 3 consecutive robots within budget, so we return 3.
Example 2:

Input: chargeTimes = [11,12,19], runningCosts = [10,8,7], budget = 19
Output: 0
Explanation: No robot can be run that does not exceed the budget, so we return 0.
 

Constraints:

chargeTimes.length == runningCosts.length == n
1 <= n <= 5 * 104
1 <= chargeTimes[i], runningCosts[i] <= 105
1 <= budget <= 1015
'''

from collections import deque
from typing import List

class Solution:
  def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
    n = len(chargeTimes)
    left = 0
    window_sum = 0
    ans = 0
    dq = deque()  # store indices of chargeTimes, decreasing order
    
    for right in range(n):
      # add new running cost
      window_sum += runningCosts[right]
      
      # maintain deque for max chargeTime
      while dq and chargeTimes[dq[-1]] <= chargeTimes[right]:
        dq.pop()
      dq.append(right)
      
      # check budget
      while dq and (chargeTimes[dq[0]] + (right - left + 1) * window_sum) > budget:
        # shrink window
        window_sum -= runningCosts[left]
        if dq[0] == left:
          dq.popleft()
        left += 1
      
      ans = max(ans, right - left + 1)
    
    return ans
  
if __name__ == "__main__":
  s = Solution()
  print(s.maximumRobots([3,6,1,3,4], [2,1,3,4,5], 25))  # 3
  print(s.maximumRobots([11,12,19], [10,8,7], 19))      # 0
