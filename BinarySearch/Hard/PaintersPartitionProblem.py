# The Painter's Partition Problem

'''
Input: arr[] = [5, 10, 30, 20, 15], k = 3
Output: 35
Explanation: The optimal allocation of boards among 3 painters is - 

Painter 1 → [5, 10] → time = 15
Painter 2 → [30] → time = 30
Painter 3 → [20, 15] → time = 35
Each painter paints a continuous block. The total time to complete the job is determined by the painter with the maximum workload, which is max(15, 30, 35) = 35.

Input: arr[] = [10, 20, 30, 40], k = 2
Output: 60
Explanation: A valid optimal partition is - 

Painter 1 → [10, 20, 30] → time = 60
Painter 2 → [40] → time = 40
The painter who finishes last determines the total time. Here, max(60, 40) = 60, which is the minimum achievable maximum time across all valid assignments.
'''
from typing import List

class Solution:
  def minimumPainterPartitionTime(self, arr: List[int], k: int) -> int:
    n = len(arr)

    if k > n:
      return -1
    
    if k == 1:
      return sum(arr)
    
    def calculateTime(time):
      no_partitions, sub_time_total = 1, 0
      
      for num in arr:
        if sub_time_total + num <= time:
          sub_time_total += num
        else:
          no_partitions += 1
          sub_time_total = num

      return no_partitions

    low, high = max(arr), sum(arr)
    answer = -1

    while low <= high:
      mid = (low + high) // 2

      if calculateTime(mid) <= k:
        answer = mid
        high = mid - 1
      else:
        low = mid + 1

    return answer


if __name__ == '__main__':
  sol = Solution()
  print(sol.minimumPainterPartitionTime(arr = [5, 10, 30, 20, 15], k = 3)) # 35
  print(sol.minimumPainterPartitionTime(arr = [10, 20, 30, 40], k = 2)) # 60
