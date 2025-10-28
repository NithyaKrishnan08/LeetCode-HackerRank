# Minimize Max Distance to Gas Station
# Difficulty: Hard
# URL: https://leetcode.com/problems/minimize-max-distance-to-gas-station/

'''
We have a horizontal number line. On that number line, we have gas stations at positions stations[0], stations[1], ..., stations[n-1]. Now, we add k more gas stations so that d, the maximum distance between adjacent gas stations, is minimized. We have to find the smallest possible value of d. Find the answer exactly to 2 decimal places.
Note: stations is in a strictly increasing order.

Examples:
Input: stations[] = [1, 2, 3, 4, 5], k = 2
Output: 1.00
Explanation: Since all gaps are already equal (1 unit each), adding extra stations in between does not reduce the maximum distance.

Input: stations[] = [3, 6, 12, 19, 33], k = 3
Output: 6.00 
Explanation: The largest gap is 14 (between 19 and 33). Adding 2 stations there splits it into approx 4.67. The next largest gap is 7 (between 12 and 19). Adding 1 station splits it into 3.5. Now the maximum gap left is 6.

Constraint:
1 ≤ stations.size() ≤ 105
0 ≤ stations[i] ≤ 106
0 ≤ k ≤ 105
'''
from typing import List
import math

class Solution:
  def minmaxGasDist(self, stations: List[int], k: int) -> float:
    n = len(stations)

    # Function to check if we can achieve max distance <= dist
    def canAchieve(dist):
      required = 0
      for i in range(1, n):
        gap = stations[i] - stations[i - 1]
        required += math.ceil(gap / dist) - 1
      return required <= k

    # Binary search on the possible maximum distance
    low, high = 0, stations[-1] - stations[0]

    while high - low > 1e-6:
      mid = (low + high) / 2
      if canAchieve(mid):
        high = mid
      else:
        low = mid

    return round(high, 2)


if __name__ == '__main__':
  sol = Solution()
  print(sol.minmaxGasDist([1, 2, 3, 4, 5], 2))      # ✅ 1.00
  print(sol.minmaxGasDist([3, 6, 12, 19, 33], 3))   # ✅ 6.00