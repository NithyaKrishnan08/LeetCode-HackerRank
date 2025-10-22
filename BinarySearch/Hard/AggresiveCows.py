# Aggresive Cows
# Difficult: Hard

# Pattern on BS: Min on Maximizing/Max on Minimizing

'''
Given an array stalls[] representing the positions of stalls and an integer k denoting the number of aggressive cows, place the cows in the stalls such that the minimum distance between any two cows is as large as possible. Return this maximum possible minimum distance.

Examples: 

Input: stalls[] = [1, 2, 4, 8, 9], k = 3
Output: 3
Explanation: We can place cow 1 at position 1, cow 2 at position 4 and cow 3 at position 9. So, the maximum possible minimum distance between two cows is 3.

Input: stalls[] = [6, 7,  9, 11, 13, 15], k = 4
Output: 2
Explanation: We can place cow 1 at position 6, cow 2 at position 9, cow 3 at position 11 and cow 4 at position 15. So, the maximum possible minimum distance between two cows is 2.
'''
from typing import List

class Solution:
  

  def aggressiveCows(self, stalls: List[int], k: int) -> int:
    def canPlaceCows(min_dist):
      count_cows = 1
      last_position = stalls[0]

      for i in range(1, len(stalls)):
        if stalls[i] - last_position >= min_dist:
          count_cows += 1
          last_position = stalls[i]

        if count_cows == k:
          return True

      return False
    
    stalls.sort()
    low, high = 1, stalls[-1] - stalls[0]
    result = 0

    while low <= high:
      mid = (low + high) // 2

      if canPlaceCows(mid):
        result = mid
        low = mid + 1
      else:
        high = mid - 1

    return result
  
if __name__ == "__main__":
  sol = Solution()
  print(sol.aggressiveCows([1, 2, 4, 8, 9], 3)) # 3
  print(sol.aggressiveCows([6, 7, 9, 11, 13, 15], 4)) # 2