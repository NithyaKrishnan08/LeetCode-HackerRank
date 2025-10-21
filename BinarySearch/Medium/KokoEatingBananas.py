# Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/description/
# Leetcode: 875
# Difficulty: Medium

'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
'''

from typing import List
import math

class Solution:
  def minEatingSpeed(self, piles: List[int], h: int) -> int:
    def calculateHours(hourly_rate):
      total_hrs = 0
      for pile in piles:
        total_hrs += math.ceil(pile / hourly_rate)

      return total_hrs

    low, high = 1, max(piles)
    ans = float('inf')

    while low <= high:
      mid = (low + high) // 2
      total_hrs = calculateHours(mid)

      if total_hrs <= h:
        ans = min(ans, mid)
        high = mid - 1
      else:
        low = mid + 1

    return ans
  
if __name__ == "__main__":
  solu = Solution()
  print(solu.minEatingSpeed([3,6,7,11], 8))  # 4
  print(solu.minEatingSpeed([30,11,23,4,20], 5))  # 30
  print(solu.minEatingSpeed([30,11,23,4,20], 6))  # 23